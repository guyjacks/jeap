"""
    1.  Read character and check if it triggers a transition
    2.  Execute transition
    3.  Executed entry procedure i.e. print { ... could use transition callbacks
    4.  Execute in procedure
    5.  Execute exit procedure print } ... could use transition callbacks

    can transition callbacks be set using decorators?...
    @self.states.obj_value.callbacks(enter=enter_func, exit=exit_func)
    self.states.obj_value

    {0}
        "key":"val",
        "key":{1}
            "val",
            "val",
            "val"
        {2}
    {3}.format(bracket_1, bracket_2, bracket_3, bracket_4)

    What is I thought of the state machine as operating on one line and I have an overarching program that generates statemachines on the fly for eachline depending on the current nesting and enclosement (arr or obj)
    s = FSM('name')
    # nested 2 deep so expecting exactly 2 tabs
    s.new.tab = 'one_tab'
    s.one_tab.tab = 'indents_complete'
    s.indents_complete.valid_char = 'key_or_val'
    s.key_or_val.valid_char = 'key_or_val'
    s.key_or_val.equal_sign = 'obj_val'
    s.key_or_val.newline = 'complete'
    s.obj_val.valid_char = 'obj_val'
    s.obj_val.newline = complete

    I could then use an simpler state machine that tracks states
"""

"""
class TypeFiniteStateMachine:
    def __init__(self):
        self.fsm = fsm.FiniteStateMachine('Unknown')
        self.fsm.unknown.space = 'unknown'
        self.fsm.unknown.tab = 'unknown'
        self.fsm.unknown.string = 'unknown'
        self.fsm.unknown.equal_sign = 'object'
        self.fsm.unknown.newline = 'array'
        self.fsm.object.
        self.fsm.array.dedent = 'end'
        self.fsm.array.end_of_input = 'end'

class LineFiniteStateMachine:
    def __init__(self):
        self.line_fsm.new.space = 'indent'
        self.line_fsm.new.tab = 'indent'
        self.line_fsm.new.newline = 'end'
        self.line_fsm.new.pound_sign = 'comment'
        self.line_fsm.new.string = 'string'

        self.line_fsm.string.string = 'string'
        self.line_fsm.string.newline = 'end'
        self.line_fsm.string.equal_sign = 'equal_sign'
        self.line_fsm.string.quote = 'open_quote'

        # check to see if this is creating a new obj or is a pair belonging to the current object
        self.line_fsm.equal_sign.string = 'string'

        self.line_fsm.open_quote.string = 'quote_contents'

        self.line_fsm.quote_contents.string = 'quote_contents'
        self.line_fsm.quote_contents.quote = 'end_quote'

        self.line_fsm.end_quote.newline = 'end'
"""


