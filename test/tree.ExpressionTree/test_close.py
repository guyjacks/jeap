import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    # 2 + 2
    assert False

def test_close_single_group(node_tree):
    # (2 + 2)
    et = tree.ExpressionTree()
    gnet = tree.ExpressionTree()
    gn = nodes.GroupNode(node_tree, gnet)
    eln_two = nodes.ExpressionLiteralNode(2, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    et.add(gn)
    et.add(eln_two)
    et.add(aon)
    et.add(eln_two)

    # close the group
    assert gn.expression.open == True
    et.close()
    assert gnet.open == False
    assert gnet.root == aon
    assert et.last_value == gn.expression
    assert aon.left == eln_two
    assert aon.right  == eln_two
    assert et.open == True

    # close the expression
    et.close()
    assert et.open == False
    assert et.root == gnet

def test_closing_nested_groups(node_tree):
    # ((2 + 2) * 2)
    et = tree.ExpressionTree()
    outer_group_tree = tree.ExpressionTree()
    outer_group = nodes.GroupNode(node_tree, outer_group_tree)
    inner_group_tree = tree.ExpressionTree()
    inner_group = nodes.GroupNode(node_tree, inner_group_tree)
    eln = nodes.ExpressionLiteralNode(2, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    mon = nodes.MultiplyOperatorNode(node_tree)
    et.add(outer_group)
    et.add(inner_group)
    et.add(eln)
    et.add(aon)
    et.add(eln)

    # close the inner group
    et.close()
    assert inner_group_tree.open == False
    assert outer_group_tree.open == True
    assert et.open == True
    assert inner_group_tree.root == aon
    assert aon.left == eln
    assert aon.right == eln

    et.add(mon)
    et.add(eln)

    # close the outer group
    et.close()
    assert outer_group_tree.open == False
    assert et.open == True
    assert outer_group_tree.root == mon
    assert mon.left == inner_group_tree
    assert mon.right == eln

    # close et
    et.close()
    assert et.open == False
    assert et.root == outer_group_tree
    assert et.last_operator == None
    assert et.last_value == outer_group_tree
