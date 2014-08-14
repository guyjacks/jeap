import jeap.context as context
import jeap.nodes as nodes
import test.test_utils as utils

def test_get_attribute():
    c = context.Context(name = "Guy Jacks")
    assert c.get('name') == 'Guy Jacks'

def test_get_member(node_tree):
    people = {}
    people['a'] = 'b'
    people['c'] = 'd'
    c = context.Context(people = people)
    a_accessor = nodes.VariableAccessorNode('a', 'member', node_tree)
    assert c.get('people', a_accessor) == 'b'

def test_get_mixed(node_tree):
    # x.y['key'].a[1]
    x = utils.ObjectX()
    y = nodes.VariableAccessorNode('y', 'attribute', node_tree)
    y_key = nodes.VariableAccessorNode('key', 'member', node_tree)
    a = nodes.VariableAccessorNode('a', 'attribute', node_tree)
    a_key = nodes.VariableAccessorNode(1, 'member', node_tree)

    c = context.Context(x = x)
    assert c.get('x', y, y_key, a, a_key) == 'b'

def test_exception():
    assert False
