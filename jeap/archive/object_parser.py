import rosie.rosie as rosie

class ObjectParser:   
    def parse_object(self, key, input, starting_indent):
        rest = input
        self.output = '{' + key + ':'
        while len(rest) > 0:
            char = input[0]
            rest = input[1:]

            type = self.interpreter.interpret(char)
            # wrap transition in try block
            state = self.fsm.transition(type)
            if state is 'pair_separator':
                pass
            if state is 'begin_arr_item_line':
                self.output += self.parse_array(buffer, rest, starting_indent)
            
        self.output += '}'

class ObjectFSM:
    def __init__(self):
        fsm = rosie.FiniteStateMachine('start')
        # end can be reached by
        ## dedent
        ## end of input

