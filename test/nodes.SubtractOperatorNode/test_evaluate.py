import jeap.tree as tree
import jeap.nodes2 as nodes

def test_evaluate_base():
    # 4 - 2
    literal_four = nodes.ExpressionLiteralNode(4)
    literal_two = nodes.ExpressionLiteralNode(2)
    sub_op = nodes.SubtractOperatorNode()
    sub_op.left = literal_four
    sub_op.right = literal_two
    assert sub_op.evaluate() == 2
