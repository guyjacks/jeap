import jeap.nodes as nodes

def test_base():
    true_node = nodes.ExpressionLiteralNode(True)
    false_node = nodes.ExpressionLiteralNode(False)
    or_node = nodes.OrOperatorNode()

    or_node.left = true_node
    or_node.right = false_node
    assert or_node.evaluate() == True

    or_node.right = true_node
    assert or_node.evaluate() == True

    or_node.left = false_node
    assert or_node.evaluate() == True

    or_node.left = false_node
    or_node.right = false_node
    assert or_node.evaluate() == False
