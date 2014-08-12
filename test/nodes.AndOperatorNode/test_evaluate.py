import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    true_node = nodes.ExpressionLiteralNode(True, node_tree)
    false_node = nodes.ExpressionLiteralNode(False, node_tree)
    and_node = nodes.AndOperatorNode(node_tree)

    and_node.left = true_node
    and_node.right = false_node
    assert and_node.evaluate() == False

    and_node.right = true_node
    assert and_node.evaluate() == True

    and_node.left = false_node
    and_node.right = false_node
    assert and_node.evaluate() == False
