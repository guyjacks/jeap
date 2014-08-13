import jeap.nodes as nodes

def test_base(node_tree):
    true_node = nodes.ExpressionLiteralNode(True, node_tree)
    false_node = nodes.ExpressionLiteralNode(False, node_tree)
    or_node = nodes.OrOperatorNode(node_tree)

    # True or False
    or_node.left = true_node
    or_node.right = false_node
    assert or_node.evaluate() == True

    # True or True
    or_node.right = true_node
    assert or_node.evaluate() == True

    # False or True
    or_node.left = false_node
    assert or_node.evaluate() == True

    # False or False
    or_node.left = false_node
    or_node.right = false_node
    assert or_node.evaluate() == False
