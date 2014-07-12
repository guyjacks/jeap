class Parser(object):
    def __init__(self):
        pass
    def parse(self, input):
        for char in input:
            self.line_char_count += 1

            # enumerated representation (int) of the state transition event
            event = self.interpreter.interpret(char)
            # string representation of the state transition event
            transition_event = self.events.get_reverse(event)

            state = self.fsm.transition(transition_event)

            #### idea for refactoring fsm
            #### state, callback, *args, **kwargs = self.fsm.transition(transition_event)
            #### if callback:
            #### callback(args, kwargs)

            """
            for index, token in enumerate(self.tokens_buffer):
                ready, type, buffer_flag, value = token
                if buffer_flag:
                    buffer_flag = False
                    value += char
                    self.tokens_buffer[index] = (ready, type, buffer_flag, value)
                if ready:
                    self.tokens_buffer.remove(index)
                    yield type, value

            """
            if self.flag_update_token_value_buffer:
                self.token_value_buffer += char
                self.__toggle_add_to_buffer_flag()

            if self.flag_tokens_ready:
                self.__toggle_token_ready_flag()
                for token_type in self.tokens_buffer:
                    if token_type == self.tokens.indent:
                        token_value = self.indent_count
                        self.__reset_indent_count()
                    elif token_type == self.tokens.newline:
                        token_value = ""
                    else:
                        token_value = self.token_value_buffer
                        self.__clear_buffer()
                yield token_type, token_value
        yield self.tokens.end_of_input, ""

    #### API Methods ####
    #### FSM will call these from its own callbacks ####

    def add_last_to_token_value_buffer(self):
        pass

    def increment_white_space_count(self, amount=1):
        pass

    def calculate_indent(self):
        pass

    def add_to_token_buffer(self):
        pass

    def tokenize(self, token_type):
        pass

    def clear_token_value_buffer(self):
        pass

    def clear_token_buffer(self):
        pass
