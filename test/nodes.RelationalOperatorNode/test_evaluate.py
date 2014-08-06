import jeap.tree as tree
import jeap.nodes2 as nodes

def test_less_than():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    lt = nodes.RelationalOperatorNode('<')

    lt.left = two
    lt.right = four
    assert lt.evaluate() == True

    lt.left = four
    lt.right = two
    assert lt.evaluate() == False

    lt.negate = True
    assert lt.evaluate() == True

def test_less_than_or_equal():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    lte = nodes.RelationalOperatorNode('<=')

    lte.left = two
    lte.right = four
    assert lte.evaluate() == True

    lte.left = four
    lte.right = two
    assert lte.evaluate() == False

    lte.negate = True
    assert lte.evaluate() == True
    
    lte.negate = False
    lte.left = four
    lte.right = four
    assert lte.evaluate() == True

def test_greater_than():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    gt = nodes.RelationalOperatorNode('>')

    gt.left = two
    gt.right = four
    assert gt.evaluate() == False

    gt.left = four
    gt.right = two
    assert gt.evaluate() == True

    gt.negate = True
    assert gt.evaluate() == False

def test_greater_than_or_equal():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    gte = nodes.RelationalOperatorNode('>=')

    gte.left = two
    gte.right = four
    assert gte.evaluate() == False

    gte.left = four
    gte.right = two
    assert gte.evaluate() == True

    gte.negate = True
    assert gte.evaluate() == False
    
    gte.negate = False
    gte.left = four
    gte.right = four
    assert gte.evaluate() == True

def test_equals():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    eq = nodes.RelationalOperatorNode('==')

    eq.left = two
    eq.right = four
    assert eq.evaluate() == False

    eq.left = two
    eq.right = two
    assert eq.evaluate() == True
    
    eq.negate = True
    assert eq.evaluate() == False

def test_not_equal():
    two = nodes.ExpressionLiteralNode(2)
    four = nodes.ExpressionLiteralNode(4)
    neq = nodes.RelationalOperatorNode('!=')

    neq.left = two
    neq.right = four
    assert neq.evaluate() == True

    neq.left = two
    neq.right = two
    assert neq.evaluate() == False

    neq.negate = True
    assert neq.evaluate() == True

