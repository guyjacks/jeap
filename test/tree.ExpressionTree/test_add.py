import jeap.tree as tree
import jeap.nodes2 as nodes

def test_add_literal():
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    et.add(literal_two)
    assert et.root == None
    assert et.last_operator == None
    assert et.last_value == literal_two

def test_add_first_operator():
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    et.add(literal_two)
    add_op = nodes.AddOperatorNode(et)
    et.add(add_op)
    assert et.root == add_op
    assert et.last_operator == add_op
    assert et.last_value == literal_two
    assert et.last_operator.left == literal_two

def test_add_lower_priority_operator():
    # 2 * 2 + 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    mul_op = nodes.MultiplyOperatorNode(et)
    add_op = nodes.AddOperatorNode(et)
    et.add(literal_two)
    et.add(mul_op)
    et.add(literal_two)
    et.add(add_op)
    
    assert et.root == add_op
    assert add_op.left == mul_op
    assert add_op.right == None
    assert mul_op.left == literal_two
    assert mul_op.right == literal_two
    assert et.last_operator == add_op

def test_add_equal_priority_operator():
    # 2 - 2 - 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    first_sub_op = nodes.SubtractOperatorNode()
    second_sub_op = nodes.SubtractOperatorNode()
    et.add(literal_two)
    et.add(first_sub_op)
    et.add(literal_two)
    et.add(second_sub_op)

    assert et.root == second_sub_op
    assert second_sub_op.left == first_sub_op
    assert second_sub_op.right == None
    assert first_sub_op.left == literal_two
    assert first_sub_op.right == literal_two
    assert et.last_operator == second_sub_op

def test_add_greater_priority_operator():
    # 2 + 2 / 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    add_op = nodes.AddOperatorNode()
    div_op = nodes.DivideOperatorNode()
    et.add(literal_two)
    et.add(add_op)
    et.add(literal_two)
    et.add(div_op)

    assert et.root == add_op
    assert add_op.left == literal_two
    assert add_op.right == div_op
    assert div_op.left == literal_two
    assert div_op.right == None
    assert et.last_operator == div_op

def test_add_group():
    # (2 + 2) x 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2)
    group_node = nodes.GroupNode(tree.ExpressionTree())
    add_op = nodes.AddOperatorNode()
    mul_op = nodes.MultiplyOperatorNode()
    et.add(group_node)
    et.add(literal_two)
    et.add(add_op)
    et.add(literal_two)
    et.close()
    et.add(mul_op)

    assert et.root == mul_op
    assert et.last_operator == mul_op
    assert et.last_value == group_node
    assert mul_op.left == group_node
    assert mul_op.right == None
    assert group_node.tree.root == add_op
    assert group_node.tree.closed == True
    assert group_node.tree.last_operator == add_op
    assert group_node.tree.last_value == literal_two
    assert add_op.left == literal_two
    assert add_op.right == literal_two
