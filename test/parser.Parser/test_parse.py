import jeap.parser as jeap
import jeap.enum_utils as eu
import jeap.interpreter as ji

def test_base():
    event_enum = eu.Events()
    token_enum = eu.Tokens()
    i = ji.Interpreter(event_enum)
    p = jeap.Parser(event_enum, token_enum, i)
    space = ' '
    tab = 4 * space

    input = '\n'
    input += '\n'
    input += 'value1\n'
    input += 'key1=value2\n'
    input += '\n'
    input += 'key2=\n'
    input += tab + 'key3=value3\n'
    input += tab + 'key4=value4\n'
    input += tab + 'key5=\n'
    input += tab + tab + 'key6=value5\n'
    input += tab + tab + 'key7=value6\n'
    input += 'value7\n'
    input += 'value8\n'
    input += tab + 'value9'


    tokens = []
    for token in p.parse(input):
        tokens.append(token)

    # test line count
    assert 14 == p.line_count

    #'\tvalue9'
    expected = token_enum.end_of_input, ''
    actual= tokens.pop()
    assert expected == actual

    expected = token_enum.literal, 'value9'
    actual= tokens.pop()
    assert expected == actual

    expected = token_enum.indent, 1
    actual= tokens.pop()
    assert expected == actual

    # 'value8\n'
    expected = token_enum.newline, ''
    actual= tokens.pop()
    assert expected == actual

    expected = token_enum.literal, 'value8'
    actual= tokens.pop()
    assert expected == actual

def test_base_w_tabs():
    # make sure that \t can be used as well
    assert True == False


def test_pair():
    event_enum = eu.Events()
    token_enum = eu.Tokens()
    i = ji.Interpreter(event_enum)
    p = jeap.Parser(event_enum, token_enum, i)
    input = 'hello=world\n'
    tokens = []
    for token in p.parse(input):
        tokens.append(token)

    expected = token_enum.end_of_input, ''
    actual = tokens.pop()
    assert expected == actual
    
    expected = token_enum.newline, ''
    actual = tokens.pop()
    assert expected == actual

    expected = token_enum.literal, 'world'
    actual = tokens.pop()
    assert expected == actual

    expected = token_enum.pair_key, 'hello'
    actual = tokens.pop()
    assert expected == actual

def test_literal():
    event_enum = eu.Events()
    token_enum = eu.Tokens()
    i = ji.Interpreter(event_enum)
    p = jeap.Parser(event_enum, token_enum, i)
    input = 'hello world\n'
    tokens = []
    for token in p.parse(input):
        tokens.append(token)

    expected = token_enum.end_of_input, ''
    actual = tokens.pop()
    assert expected == actual
    
    expected = token_enum.newline, ''
    actual = tokens.pop()
    assert expected == actual

    expected = token_enum.literal, 'hello world'
    actual = tokens.pop()
    assert expected == actual

def test_single_indent():
    event_enum = eu.Events()
    token_enum = eu.Tokens()
    i = ji.Interpreter(event_enum)
    p = jeap.Parser(event_enum, token_enum, i)
    space = ' '
    indent = 4 * space
    input = indent + 'hello world'
    tokens = []
    for token in p.parse(input):
        tokens.append(token)
    
    expected = token_enum.end_of_input, ''
    actual = tokens.pop()
    assert expected == actual
    
    expected = token_enum.literal, 'hello world'
    actual = tokens.pop()
    assert expected == actual

    expected = token_enum.indent, 1
    actual = tokens.pop()
    assert expected == actual

def test_multiple_indent():
    event_enum = eu.Events()
    token_enum = eu.Tokens()
    i = ji.Interpreter(event_enum)
    p = jeap.Parser(event_enum, token_enum, i)
    space = ' '
    indents = 8 * space
    input = indents + 'hello world'
    tokens = []
    for token in p.parse(input):
        tokens.append(token)
    
    expected = token_enum.end_of_input, ''
    actual = tokens.pop()
    assert expected == actual
    
    expected = token_enum.literal, 'hello world'
    actual = tokens.pop()
    assert expected == actual

    expected = token_enum.indent, 2
    actual = tokens.pop()
    assert expected == actual

def test_improper_indentation():
    assert True == False
