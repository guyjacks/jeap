import jeap.context as context
import jeap.nodes as nodes

class ObjectX(object):
    def __init__(self):
        self.y = {'key': ObjectC()}

class ObjectC(object):
    def __init__(self):
        self.a = ['a', 'b', 'c']

def test_get_attribute():
    c = context.Context(name = "Guy Jacks")
    assert c.get('name') == 'Guy Jacks'

def test_get_member():
    people = {}
    people['a'] = 'b'
    people['c'] = 'd'
    c = context.Context(people = people)
    a_accessor = nodes.VariableAccessorNode('a', 'member')
    assert c.get('people', a_accessor) == 'b'

def test_get_mixed():
    # x.y['key'].a[1]
    x = ObjectX()
    y = nodes.VariableAccessorNode('y', 'attribute')
    y_key = nodes.VariableAccessorNode('key', 'member')
    a = nodes.VariableAccessorNode('a', 'attribute')
    a_key = nodes.VariableAccessorNode(1, 'member')

    c = context.Context(x = x)
    assert c.get('x', y, y_key, a, a_key) == 'b'

def test_exception():
    assert False
