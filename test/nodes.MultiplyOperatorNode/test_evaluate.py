import jeap.tree as tree
import jeap.nodes as nodes

def test_evaluate_base(node_tree):
    # 4 * 2
    literal_four = nodes.ExpressionLiteralNode(4, node_tree)
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    mul_op = nodes.MultiplyOperatorNode(node_tree)
    mul_op.left = literal_four
    mul_op.right = literal_two
    assert mul_op.evaluate() == 8

def test_multiply_two_groups(node_tree):
    # (2 + 2) x (4 - 2)
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    literal_four = nodes.ExpressionLiteralNode(4, node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
    mul_op = nodes.MultiplyOperatorNode(node_tree)
    sub_op = nodes.SubtractOperatorNode(node_tree)
    group_one_tree = tree.ExpressionTree()
    group_two_tree = tree.ExpressionTree()

    add_op.left = literal_two
    add_op.right = literal_two

    sub_op.left = literal_four
    sub_op.right = literal_two

    group_one_tree.root = add_op
    group_two_tree.root = sub_op
    
    mul_op.left = group_one_tree
    mul_op.right = group_two_tree

    assert mul_op.evaluate() == 8
