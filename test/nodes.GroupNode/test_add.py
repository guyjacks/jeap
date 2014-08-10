import jeap.tree as tree
import jeap.nodes as nodes

def test_base():
    t = tree.NodeTree()
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(t, et)
    gnet = tree.ExpressionTree()
    gn = nodes.GroupNode(t, gnet)
    en.add()
    gn.add()

    # make sure tree scope was properly updated
    # root, value, expression
    assert len(t.scope) == 3
    assert gn not in t.scope
    # make sure gn was properly added to en
    assert en.expression.expression.last_value == gn
    assert en.expression.expression.group == True
    # make sure gn was properly initialized
    # gn should have its own new expression tree
    assert gn.expression != en.expression.expression
    assert gn.expression.last_operator == None
    assert gn.expression.last_value == None
    assert gn.expression.group == False
