import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    # {{ x }}
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    vn = nodes.ExpressionVariableNode('x', node_tree)
    en.add()
    vn.add()

    assert et.last_value == vn
    assert vn not in node_tree.scope
