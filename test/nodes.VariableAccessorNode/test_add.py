import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    en = nodes.ExpressionNode(node_tree, tree.ExpressionTree())
    evn = nodes.ExpressionVariableNode('x', node_tree)
    y_van = nodes.VariableAccessorNode('y', 'attribute')
    y_key_van = nodes.VariableAccessorNode('key', 'member)
    en.add()
    evn.add()
    y_van.add()
    y_key_van.add()

    assert len(node_tree.scope) == 2
