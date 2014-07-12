import pytest
from jeap.indent_parser import IndentParser

@pytest.fixture
def ip():
    # standard indent parser
    spaces_per_indent = 4
    ip = IndentParser()
    return ip

@pytest.fixture
def space():
    return ' '

@pytest.fixture
def spaces_per_indent():
    return 4

@pytest.fixture
def indent():
    return '    '

def test_single_indent(ip, spaces_per_indent, space, indent):
    input = indent + 'key=value'
    indent_count, char, pos = ip.parse(input, 0, spaces_per_indent)
    expected = 1
    assert expected == indent_count
    expected = 'k'
    assert expected == char
    expected = 5
    assert expected == 5

def test_zero_indents(ip, spaces_per_indent, space, indent):
    input = 'key=value'
    indent_count, char, pos = ip.parse(input, 0, spaces_per_indent)
    expected = 0
    assert expected == indent_count
    expected = 'k'
    assert expected == char
    expected = 1
    assert expected == pos

def test_two_indents(ip, spaces_per_indent, space, indent):
    input = indent + indent + 'key=value'
    indent_count, char, pos = ip.parse(input, 0, spaces_per_indent)
    expected = 2
    assert expected == indent_count
    expected = 'k'
    assert expected == char
    expected = 9
    assert expected == pos

def test_incomplete_indent(ip, spaces_per_indent, space, indent):
    incomplete_indent = 2 * space
    input = incomplete_indent + 'key=value'
    actual, char, pos = ip.parse(input, 0, spaces_per_indent)
    assert True == False
