import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    nn = nodes.NegateNode(node_tree)
    en.add()
    assert et.negate_next == False
    nn.add()
    assert et.negate_next == True
