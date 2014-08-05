import jeap.tree as tree
import jeap.nodes2 as nodes

def test_evaluate_base():
    # 4 * 2
    literal_four = nodes.ExpressionLiteralNode(4)
    literal_two = nodes.ExpressionLiteralNode(2)
    mul_op = nodes.MultiplyOperatorNode()
    mul_op.left = literal_four
    mul_op.right = literal_two
    assert mul_op.evaluate() == 8

def test_multiply_two_groups():
    # (2 + 2) x (4 - 2)
    literal_two = nodes.ExpressionLiteralNode(2)
    literal_four = nodes.ExpressionLiteralNode(4)
    add_op = nodes.AddOperatorNode()
    mul_op = nodes.MultiplyOperatorNode()
    sub_op = nodes.SubtractOperatorNode()
    group_one = nodes.GroupNode(tree.ExpressionTree())
    group_two = nodes.GroupNode(tree.ExpressionTree())

    group_one.add_to_expression(literal_two)
    group_one.add_to_expression(add_op)
    group_one.add_to_expression(literal_two)
    group_one.close()

    group_two.add_to_expression(literal_four)
    group_two.add_to_expression(sub_op)
    group_two.add_to_expression(literal_two)
    group_two.close()

    mul_op.left = group_one
    mul_op.right = group_two

    assert mul_op.evaluate() == 8
