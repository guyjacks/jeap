import jeap.tree as tree
import jeap.nodes as nodes
import jeap.context as context
import test.test_utils as utils

def test_base(node_tree):
    x = utils.ObjectX()
    c = context.Context(x = x)

    x_evn = nodes.ExpressionVariableNode('x', node_tree)
    y_van = nodes.VariableAccessorNode('y', 'attribute', node_tree)
    y_key_van = nodes.VariableAccessorNode('key', 'member', node_tree)
    a_van = nodes.VariableAccessorNode('a', 'attribute', node_tree)
    a_key_van = nodes.VariableAccessorNode(1, 'member', node_tree)
    x_evn.add_child(y_van)
    x_evn.add_child(y_key_van)
    x_evn.add_child(a_van)
    x_evn.add_child(a_key_van)
    assert x_evn.evaluate(c) == 'b'

def test_negate(node_tree):
    assert False
