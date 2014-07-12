def parse(input, pos):
    size = len(input)
    while pos < size:
        char = input[pos]
        type = interpret(char)
        fsm.transition(type)
