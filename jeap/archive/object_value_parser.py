class ObjectValueFsm:
    """
        an object value is either a pair value, a nested array or a nested object
    """
    def __init__(self):
        # already found pair separator so we're trying to determine the value type
        # nested value or pair value
        self.fsm = fsm.FiniteStateMachine('unknown_value')

        # key=^value where ^ is a space
        # clear spaces after the pair separator
        self.fsm.unknown_value.space = 'unknown_value'

        # key=^alue where ^ is 'v'
        # if the next char is a string then we know its the beginning of a text value in key:value
        self.fsm.unknown_value.string = 'text_value'
        
        # key=^ where ^ is a newline
        #     value should be nested on the following lines
        # a newline following the separator indicates a nested value
        self.fsm.unknown_value.newline = 'begin_nested_value_line'

        # key=v...^...alue where ^ is any valid string char
        # keep eating through string chars
        self.fsm.text_value.string = 'text_value'

        # key=value^ where ^ is a newline
        self.fsm.text_value.newline = 'begin_pair'

        # ^key=value
        # getting the key
        # a newline is an error because an array item can only exist in the pair value
        self.fsm.begin_pair.string = 'begin_pair'
        self.fsm.begin_pair.pair_separator = 'unknown_value'

        # anything besides an indent is an error
        self.fsm.begin_nested_value_line.indent = 'begin_nested_value'

        # either gonna be a nested object pair or a nested array item
        self.fsm.begin_nested_value.string = 'unknown_nested_value'
        self.fsm.begin_nested_value.indent = 'error' # cannot double indent

        self.fsm.unknown_nested_value.string = 'unknown_nested_value'
        # the first nested line contained an array item
        self.fsm.unknown_nested_value.newline = 'begin_arr_item_line'
        # the first nested line contains an object pair
        self.fsm.unknown_nested_value.equal_sign = 'unknown_value'

    def transition(self, event):
        return self.fsm.transition(event)


