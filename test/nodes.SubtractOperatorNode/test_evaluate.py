import jeap.tree as tree
import jeap.nodes as nodes

def test_evaluate_base(node_tree):
    # 4 - 2
    literal_four = nodes.ExpressionLiteralNode(4, node_tree)
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    sub_op = nodes.SubtractOperatorNode(node_tree)
    sub_op.left = literal_four
    sub_op.right = literal_two
    assert sub_op.evaluate() == 2
