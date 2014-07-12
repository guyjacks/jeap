import rosie.rosie as rosie
import compiler
import enum_utils
import interpreter
import parser
import nodes

class JEAP(object):
    def __init__(self, spaces_per_indent=4, template_dir=None):
        # REFACTOR: rename events to something more meaningful
        events = eu.Events()
        tokens = eu.Tokens()
        interpreter = interpreter.Interpreter(events)
        parser = parser.Parser(events, tokens, interpreter, spaces_per_indent)
        # initialize linker
        self.ast = nodes.Nodes()
        self.fsm = compiler.JeapCompilerFSM(tokens, self.ast)

    def parse_and_compile(self, input):
        for token in self.parser.parse(input):
            tok_type, tok_value = token
            self.fsm.transition(tok_type, tok_value)

    def render(self, template, filters = {}, **data):
        """
            data holds the data available to the template
            REFACTOR - could convert data to superbunch
        """
        self.parse_and_compile(template)
        return self.ast.render(data, self.filters)

    def register_filter(self, name, func):
        pass

    def create_node(self, type, value):
        pass
