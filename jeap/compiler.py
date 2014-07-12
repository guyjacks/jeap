import rosie.rosie as rosie

class JeapCompilerFSM(object):
    def __init__(tokens, ast, node_factory):
        """ tokens must be an enum """
        self.tokens = tokens
        self.ast = ast
        # node_factory is a function
        self.node_factory.tree = ast
        self.current_value = None
        self.fsm = self.create()

    def transition(self, token_type, token_value=None):
        if value is not None:
            self.current_value = value
        self.fsm.transition(token_type)

    def create(self):
        # Shorten tokens to avoid typing self.tokens.token
        tok_indent = self.tokens.indent
        tok_pair_key = self.tokens.pair_key
        tok_literal = self.tokens.literal
        tok_newline = self.tokens.newline

        # Alias callback methods to avoid typing out self.__method_name()
        nodify = self.__nodify
        indent = self.__indent

        fsm = rosie.FiniteStateMachine('start')

        # Ignore whitespace at the beginning of input
        fsm.start.on(tok_newline).go('start')
        fsm.start.on(tok_indent).go('start')
        fsm.start.on(tok_literal).go('item_or_pair')
        # fsm.start.on(tok_variable).go('item_or_pair')

        fsm.item_or_pair.on(tok_literal).go('item_or_pair')
        #fsm.item_or_pair.on(tok_variable).go('item_or_pair')
        fsm.item_or_pair.on(tok_newline).go('array_item').do(nodify)
        fsm.item_or_pair.on(tok_separator).go('pair_value')

        # may need to rename to begin new array item
        fsm.array_item.on(tok_newline).go('array_item')
        fsm.array_item.on(tok_literal).go('item_or_pair')
        #fsm.array_item.on(tok_variable).go('item_or_pair')
        fsm.array_item.on(tok_indent).go('????')

        fsm.pair_value.on(tok_literal).go('pair_value_literal')
        #fsm.pair_value.on(tok_variable).go('pair_value_literal')
        fsm.pair_value.on(tok_newline).go('pair_value_nested')

        fsm.pair_value_literal.on(tok_literal).go('pair_value_literal')
        #fsm.pair_value_literal.on(tok_variable).go('pair_value_literal')
        fsm.pair_value_literal.on(tok_newline).go('item_or_pair')

        fsm.pair_value_nested.on(tok_indent).go('item_or_pair').do(indent)

        return fsm

    ##################################
    #### Begin callback functions ####
    ##################################

    def __indent(self, token_type):
        # current_token_value should be an int counting the # of indents
        nest = self.current_nest_level - self.current_token_value
        if nest == 1:
            # indented
            parent_node = self.json_scope_stack[-1]
            # create a parent node and add to scope_stack
            # the parent is either an array or an object
            # the type will be determined by the next created node
            new_parent_node = syntax_tree.Node()
            parent_node.add_child(new_parent_node)
            self.json_scope_stack.append(parent_node)
            # pass skip to nodify since its designed to be called by the state machine
            self.__nodify(token_type)
        elif nest == -1:
            # dedented
            # pseudo: close the scope on the sytax tree
            self.__nodify(token_type)
        elif nest = 0:
            # not indented
            self.__nodify(token_type)
        else:
            # throw error
            pass
            
        self.indent_count == 0

    def __nodify(self, type):
        node = self.node_factory.create(type, self.current_value)
        self.ast.add_node(node)

    def __close_scope(self):
        self.ast.close_scope()

    def __close_all_scope(self):
        # called when end of input is reached
        self.ast.end()
        pass
