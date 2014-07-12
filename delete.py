class Jeap(object):
    def __init__(self):
        events = Events()
        tokens = Tokens()
        parser_state_machine = ParserStateMachine(events, tokens)
        parser = Parser(events, tokens, parser_state_machine)
        compiler_state_machine = CompilerStateMachine(tokens)
        ast = Nodes()
        compiler = Compiler(tokens, parser, compiler_state_machine, ast)
