import jeap.interpreter as interpreter
import jeap.char_type as char_type

def test_alphabet_characters():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.string
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for character in alphabet:
        actual = i.interpret(character)
        assert expected == actual

def test_digits():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.digit
    digits = '0123456789'   
    for digit in digits:
        actual = i.interpret(digit)
        assert expected == actual

def test_interpret_newline():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.newline
    input = '\n'
    actual = i.interpret(input)
    assert expected == actual

def test_interpret_space():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.space
    input = ' '
    actual = i.interpret(input)
    assert expected == actual

def test_interpret_pair_separator():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.pair_separator
    input = '='
    actual = i.interpret(input)
    assert expected == actual

def test_brackets():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.open_bracket
    input = '['
    actual = i.interpret(input)
    assert expected == actual

    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.close_bracket
    input = ']'
    actual = i.interpret(input)
    assert expected == actual

def test_curly_braces():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.open_curly_brace
    input = '{'
    actual = i.interpret(input)
    assert expected == actual

    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.close_curly_brace
    input = '}'
    actual = i.interpret(input)
    assert expected == actual

def test_quote():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.quote
    input = '"'
    actual = i.interpret(input)
    assert expected == actual

def test_pound():
    ct = char_type.CharType()
    i = interpreter.Interpreter(ct)
    expected = ct.pound
    input = '#'
    actual = i.interpret(input)
    assert expected == actual

def test_space():
    assert True == False

def test_tab():
    assert True == False

def test_i88n_characters():
    assert True == False
