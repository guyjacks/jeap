import jeap.tree as tree
import jeap.nodes as nodes

def test_add_after_lower_priority_operator(node_tree):
    # 2 + 2 * 
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    eln = nodes.ExpressionLiteralNode(2, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    mon = nodes.MultiplyOperatorNode(node_tree)
    en.add()
    eln.add()
    aon.add()
    eln.add()
    mon.add()

    assert et.root == aon
    assert et.last_operator == mon
    assert aon.right == mon
    assert mon.left == eln
