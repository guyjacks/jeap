import jeap.tree as tree
import jeap.nodes as nodes

def test_less_than(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    lt = nodes.RelationalOperatorNode('<', node_tree)

    lt.left = two
    lt.right = four
    assert lt.evaluate() == True

    lt.left = four
    lt.right = two
    assert lt.evaluate() == False

def test_less_than_or_equal(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    lte = nodes.RelationalOperatorNode('<=', node_tree)

    lte.left = two
    lte.right = four
    assert lte.evaluate() == True

    lte.left = four
    lte.right = two
    assert lte.evaluate() == False

    lte.left = four
    lte.right = four
    assert lte.evaluate() == True

def test_greater_than(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    gt = nodes.RelationalOperatorNode('>', node_tree)

    gt.left = two
    gt.right = four
    assert gt.evaluate() == False

    gt.left = four
    gt.right = two
    assert gt.evaluate() == True

def test_greater_than_or_equal(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    gte = nodes.RelationalOperatorNode('>=', node_tree)

    gte.left = two
    gte.right = four
    assert gte.evaluate() == False

    gte.left = four
    gte.right = two
    assert gte.evaluate() == True

    gte.left = four
    gte.right = four
    assert gte.evaluate() == True

def test_equals(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    eq = nodes.RelationalOperatorNode('==', node_tree)

    eq.left = two
    eq.right = four
    assert eq.evaluate() == False

    eq.left = two
    eq.right = two
    assert eq.evaluate() == True

def test_not_equal(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    neq = nodes.RelationalOperatorNode('!=', node_tree)

    neq.left = two
    neq.right = four
    assert neq.evaluate() == True

    neq.left = two
    neq.right = two
    assert neq.evaluate() == False

def test_in(node_tree):
    two = nodes.ExpressionLiteralNode(2, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    list_node = nodes.ExpressionLiteralNode(node_tree, [1, 2, 3])
    in_op = nodes.RelationalOperatorNode('in', node_tree)

    in_op.left = two
    in_op.right = list_node
    assert in_op.evaluate() == True

    in_op.left = four
    assert in_op.evaluate() == False
