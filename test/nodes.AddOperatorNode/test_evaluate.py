import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    # 2 + 2
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
    add_op.left = literal_two
    add_op.right = literal_two
    assert add_op.evaluate() == 4

def test_add_groups(node_tree):
    # (2 + 2) + (2 + 2)
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    group_one_tree = tree.ExpressionTree()
    group_two_tree = tree.ExpressionTree()
    first_add = nodes.AddOperatorNode(node_tree)
    second_add = nodes.AddOperatorNode(node_tree)
    third_add = nodes.AddOperatorNode(node_tree)
    first_add.left = literal_two
    first_add.right = literal_two
    second_add.left = group_one_tree
    second_add.right = group_two_tree
    third_add.left = literal_two
    third_add.right = literal_two
    group_one_tree.root = first_add
    group_two_tree.root = third_add
    assert 8 == second_add.evaluate()
