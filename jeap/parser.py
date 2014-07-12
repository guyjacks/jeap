import rosie.rosie as rosie
class Parser(object):
    def __init__(self, event_enum, token_enum, interpreter, spaces_per_indent = 4):
        # Configuration
        self.events = event_enum
        self.tokens = token_enum
        self.interpreter = interpreter
        self.spaces_per_indent = spaces_per_indent
        
        # track line and character positioning
        self.line_count = 1
        self.line_char_count = 1

        self.flag_update_token_value_buffer = False
        self.flag_tokens_ready = False

        self.token_value_buffer = ""
        self.tokens_buffer = []

        self.indent_space_count = 0
        self.indent_count = 0

        # REFACTOR: pass fsm into initializer
        self.fsm = self.__create_states()
    
    def parse(self, input):
        for char in input:
            self.line_char_count += 1

            # enumerated representation (int) of the state transition event
            event = self.interpreter.interpret(char)
            # string representation of the state transition event
            transition_event = self.events.get_reverse(event)

            state = self.fsm.transition(transition_event)
            print('char', char, 'state', state)

            self.update_token_value_buffer(char)

            for token in self.emit_ready_tokens():
                yield token

        self.fsm.transition('end_of_input')
        self.update_token_value_buffer(char)
        for token in self.emit_ready_tokens():
            yield token
        yield self.tokens.end_of_input, ""

    def update_token_value_buffer(self, char):
        if self.flag_update_token_value_buffer:
            self.token_value_buffer += char
            self.__reset_flag_update_token_value_buffer()

    # REFACTOR: rename to prepare_ready_tokens
    def emit_ready_tokens(self):
        if self.flag_tokens_ready:
            self.__reset_flag_tokens_ready()
            for token_type in self.tokens_buffer:
                if token_type == self.tokens.indent:
                    token_value = self.indent_count
                    # REFACTOR: may not need to clear here since
                    # begin_line() resets the indent count
                    self.__reset_indent_count()
                elif token_type == self.tokens.newline:
                    token_value = ""
                else:
                    token_value = self.token_value_buffer
                    self.__clear_buffer()
                print('yield', self.tokens.get_reverse(token_type), token_value)
                yield token_type, token_value
            self.__clear_tokens_buffer()

    def __clear_buffer(self):
        self.token_value_buffer = ""

    def __clear_tokens_buffer(self):
        self.tokens_buffer = []

    def __reset_line_char_count(self):
        self.line_char_count = 1

    def __reset_indent_space_count(self):
        self.indent_space_count = 0

    def __reset_indent_count(self):
        self.indent_count = 0

    def __reset_flag_update_token_value_buffer(self):
        self.flag_update_token_value_buffer = False

    def __reset_flag_tokens_ready(self):
        self.flag_tokens_ready = False
            
    def __create_states(self):
        # Shorten the event names to avoid typing quotes
        text = 'text'
        digit = 'digit'
        space = 'space'
        newline = 'newline'
        pair_separator = 'pair_separator'
        comment_symbol = 'comment_symbol'
        end_of_input = 'end_of_input'
        
        # Alias callback methods to avoid typing out self.__method_name()
        # REFACTOR: rename to match naming converntions in rest of code
        buffer = self.__buffer
        begin_line = self.__begin_line
        count_space = self.__count_space
        tokenize = self.__tokenize
        tokenize_indents = self.__tokenize_indents
        tokenize_last_token = self.__tokenize_text_and_newline

        # Shorten token types to avoid typing self.tokens.token
        tok_pair_key = self.tokens.pair_key
        tok_literal = self.tokens.literal
        tok_newline = self.tokens.newline
        tok_indent = self.tokens.indent

        fsm = rosie.FiniteStateMachine('start_new_line')

        fsm.start_new_line.on(newline).go('start_new_line').do(begin_line)
        fsm.start_new_line.on(comment_symbol).go('comment')
        fsm.start_new_line.on(space).go('indents').do(count_space)
        fsm.start_new_line.on(text).go('key_or_value').do(buffer)
        fsm.start_new_line.on(digit).go('key_or_value').do(buffer)
        fsm.start_new_line.on(end_of_input).go('end')

        # REFACTOR: rename to buffer_pair_key_or_item_value
        fsm.key_or_value.on(text).go('key_or_value').do(buffer)
        fsm.key_or_value.on(digit).go('key_or_value').do(buffer)
        fsm.key_or_value.on(space).go('key_or_value').do(buffer)
        fsm.key_or_value.on(pair_separator).go('key_found').do(tokenize, tok_pair_key)
        fsm.key_or_value.on(newline).go('start_new_line').do(tokenize_last_token, tok_literal)
        fsm.key_or_value.on(end_of_input).go('end').do(tokenize, tok_literal)

        # REFACTOR: rename to pair_key_found
        fsm.key_found.on(text).go('building_literal').do(buffer)
        fsm.key_found.on(digit).go('building_literal').do(buffer)
        fsm.key_found.on(newline).go('start_new_line').do(begin_line)
        
        # REFACTOR: rename to buffering_text_value
        fsm.building_literal.on(text).go('building_literal').do(buffer)
        fsm.building_literal.on(digit).go('building_literal').do(buffer)
        fsm.building_literal.on(newline).go('start_new_line').do(tokenize_last_token, tok_literal)

        fsm.indents.on(newline).go('start_new_line').do(begin_line)
        fsm.indents.on(comment_symbol).go('comment')
        fsm.indents.on(space).go('indents').do(count_space)
        fsm.indents.on(text).go('key_or_value').do(tokenize_indents)
        fsm.indents.on(digit).go('key_or_value').do(tokenize_indents)

        return fsm

    ##################################
    #### Begin callback functions ####
    ##################################

    # Callback functions will be called by the fsm during transitions

    def __buffer(self):
        self.flag_update_token_value_buffer = True

    def __begin_line(self):
        self.line_count += 1
        self.__reset_line_char_count()
        self.__reset_indent_space_count()
        self.__reset_indent_count()
        self.__tokenize(self.tokens.newline)

    def __count_space(self):
        self.indent_space_count += 1

    def __tokenize_text_and_newline(self, token_type):
        self.__tokenize(token_type)
        self.__begin_line()

    def __tokenize_indents(self):
        mod = self.indent_space_count %self.spaces_per_indent
        if mod == 0:
            self.indent_count = self.indent_space_count / self.spaces_per_indent
            # a non-whitespace event indicates the end of indentation
            # we must add this non-whitespace character to the buffer
            self.flag_update_token_value_buffer = True
            self.__tokenize(self.tokens.indent)
            # REFACTOR: May be redundant with begin_line()
            self.__reset_indent_space_count()
        else:
            # raise error for incorrect number of spaces
            pass

    # fsm will call this function when certain states are reached
    # the parse function checks for tokens during each loop
    # if the parse function finds a token is ready then it yields 
    # a token tuple (token type, token value)
    def __tokenize(self, token_type):
        self.tokens_buffer.append(token_type)
        self.flag_tokens_ready = True
