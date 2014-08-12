import jeap.tree as tree
import jeap.nodes as nodes

def test_add_first_operator(node_tree):
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    eln = nodes.ExpressionLiteralNode(2, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    en.add()
    eln.add()
    aon.add()

    assert et.last_operator == aon
    assert et.root == aon
    assert aon.left == eln

def test_add_after_higher_or_equal_priority_operator(node_tree):
    # 2 * 2 +
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    eln = nodes.ExpressionLiteralNode(2, node_tree)
    mon = nodes.MultiplyOperatorNode(node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    en.add()
    eln.add()
    mon.add()
    eln.add()
    aon.add()

    assert et.last_operator == aon
    assert et.root == aon
    assert mon.right == eln
    assert aon.left == mon

def test_add_to_group(node_tree):
    # (2 + 
    et = tree.ExpressionTree()
    group_et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    gn = nodes.GroupNode(node_tree, group_et)
    eln = nodes.ExpressionLiteralNode(2, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    en.add()
    gn.add()
    eln.add()
    aon.add()

    # ensure aon was added to gn
    assert gn.expression.last_operator == aon
    assert aon.left == eln
    # ensure aon was not added to et
    assert et.last_operator != aon
