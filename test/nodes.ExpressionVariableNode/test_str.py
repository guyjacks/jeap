import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    x_evn = nodes.ExpressionVariableNode('x', node_tree)
    y_van = nodes.VariableAccessorNode('y', 'attribute', node_tree)
    z_van = nodes.VariableAccessorNode('z', 'member', node_tree)
    x_evn.add_child(y_van)
    x_evn.add_child(z_van)
    assert str(x_evn) == 'x.y[z]'
