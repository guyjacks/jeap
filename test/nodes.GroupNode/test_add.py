import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    # (
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    gnet = tree.ExpressionTree()
    gn = nodes.GroupNode(node_tree, gnet)
    en.add()
    gn.add()

    # make sure tree scope was properly updated
    # root, value, expression
    assert len(node_tree.scope) == 3
    assert gn not in node_tree.scope
    # make sure gn was properly added to en
    assert en.expression.last_value == gn.expression
    assert en.expression.last_value.negate == False
    # make sure gn was properly initialized
    # gn should have its own new expression tree
    assert gn.expression != en.expression
    assert gn.expression.last_operator == None
    assert gn.expression.last_value == None

def test_add_to_group(node_tree):
    # ((2 + 2) * 2)
    assert False

def test_add_after_negate(node_tree):
    # not (
    assert False
