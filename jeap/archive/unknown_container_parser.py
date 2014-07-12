class UnknownContainerParser:
    def parse_unknown(self, buffer, input):
        # should parse the first few characters until a separator or newline is found
        # this will determine if we are inside of an array or an object
        for char in input:
            type = self.interpreter.interpret(char)
            state = self.fsm.transition(type)
            if state is 'pair_separator':
                self.output += self.parse_object(buffer, rest, starting_indent)
            if state is 'completed_array_item':
                pass
 

class UnknownContainerFsm:
    def __init__(self):
        self.fsm = fsm.FiniteStateMachine()
        
        # a string character indicates a pair key or an array value
        self.fsm.start.string = 'object_pair_key_or_array_value'
        # a blank line should be ignored
        self.fsm.start.newline = 'start'
        self.fsm.start.space = 'indent'
        self.fsm.start.tab = 'indent'
        
        # any string characters preceding a pair separator or newline can still be a pair key or array value
        self.fsm.object_pair_key_or_array_value.string = 'object_pair_key_or_array_value'
        self.fsm.object_pair_key_or_array_value.equal_sign = 'pair_separator'
        self.fsm.object_pair_key_or_array_value.newline = 'completed_array_item'
 
