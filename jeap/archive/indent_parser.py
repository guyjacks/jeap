class IndentParser:
    def __init__(self, spaces_per_indent):
        self.fsm = SpaceIndentFSM(spaces_per_indent)

    def parse(self, input):
        rest = input
        for c in rest:
            if c is ' ':
                state = self.fsm.transition('space')
                if state is 'indent_counted':
                    self.indents += 1 
            else:
                state = self.fsm.transition('nonspace') 

class SpaceIndentFsm:
    """ unit test ideas """
    """
        test spaces_per_indent = 1
        test spaces_per_indent = 2
        test spaces_per_indent = 3
        test spaces_per_indent = 4
    """
    """ refactor """
    """ 
        since 4 spaces is so common use a prebuilt fsm for this situation
        simplify the code by creating prebuilt state machines for 1 & 2 space indents
    """
    def __init__(self, spaces_per_indent):
        self.fsm = self.__create_state_machine(spaces_per_indent)

    def transition(self, tranisition='space'):
        return self.fsm.transition(transition)

    def __create_state_machine(self, spaces_per_indent):

        # Do not want to expose these functions in the api since they will confuse end users and are not useful outside of creating the internally used state machine
        def add_space_x_state(self, state_machine, x):
            state_name = "space_%x" % x
            transition - 'space'
            destination_state_name = "space_%y" % str(x + 1)
            state_machine.add_state(state_name, transition, destination_state_name)

        def add_second_to_last_state(self, state_machine, x):
            state_name = "space_%x" % x
            transition = 'space'
            destination_state_name = 'indent_counted'
            state_machine.add_state(state_name, transition, destination_state_name)


        state_machine = fsm.FiniteStateMachine('start')
        state_machine.start.space = 'space_1'
        state_machine.start.nonspace = 'end'
 
        i = 1
        # The final space requires a new state so we'll create it after the loop
        while i < (spaces_per_indent):
            # dynamically create states for each space required to create an indent
            if i == (spaces_per_indent - 1):
                # the next to final space must transition to the indent_counted state
                self.add_second_to_last_state(self, state_machine, i)
            else:
                self.create_space_x_state(state_machine, i)
            i = i + 1
        
        # a space following the indent indicates the start of another indent
        state_machine.indent_counted.space = 'space_1'

        # no more indents
        state_machine.indent_counted.newline = 'end'
        state_machine.indent_counted.string = 'end'
        return state_machine
