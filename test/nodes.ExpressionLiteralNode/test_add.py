import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    eln = nodes.ExpressionLiteralNode(2, node_tree, et)
    en.add()
    eln.add()

    assert et.last_value == eln
