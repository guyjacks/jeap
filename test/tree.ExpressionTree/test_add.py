import jeap.tree as tree
import jeap.nodes as nodes

def test_add_literal(node_tree):
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    et.add(literal_two)
    assert et.root == None
    assert et.last_operator == None
    assert et.last_value == literal_two

def test_add_variable(node_tree):
    assert False

def test_add_first_operator(node_tree):
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
    et.add(literal_two)
    et.add(add_op)
    assert et.root == add_op
    assert et.last_operator == add_op
    assert et.last_value == literal_two
    assert et.last_operator.left == literal_two

def test_add_lower_priority_operator(node_tree):
    # 2 * 2 + 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    mul_op = nodes.MultiplyOperatorNode(node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
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

def test_add_equal_priority_operator(node_tree):
    # 2 - 2 - 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    first_sub_op = nodes.SubtractOperatorNode(node_tree)
    second_sub_op = nodes.SubtractOperatorNode(node_tree)
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

def test_add_greater_priority_operator(node_tree):
    # 2 + 2 / 
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
    div_op = nodes.DivideOperatorNode(node_tree)
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

def test_add_group(node_tree):
    assert False

def test_add_operator_to_open_group(node_tree):
    # (2 + 2) 
    et = tree.ExpressionTree()
    group_tree = tree.ExpressionTree()
    group_node = nodes.GroupNode(node_tree, group_tree)
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    add_op = nodes.AddOperatorNode(node_tree)
    et.add(group_node)
    et.add(literal_two)
    et.add(add_op)
    et.add(literal_two)
    et.close()

    assert et.root == None
    assert et.last_operator == None
    assert et.last_value == group_tree
    assert et.open == True
    assert group_tree.root == add_op
    assert group_tree.open == False 
    assert group_tree.last_operator == add_op
    assert group_tree.last_value == literal_two
    assert add_op.left == literal_two
    assert add_op.right == literal_two

def test_add_operator_after_closed_group(node_tree):
    assert False

def test_add_literal_to_open_group(node_tree):
    assert False

def test_add_literal_after_closed_group(node_tree):
    assert False

def test_add_negate_node_before_literal(node_tree):
    et = tree.ExpressionTree()
    negate_node = nodes.NegateNode(node_tree)
    false_node = nodes.ExpressionLiteralNode(False, node_tree)
    et.add(negate_node)
    et.add(false_node)
    assert false_node.negate == True

def test_add_negate_node_before_group(node_tree):
    et = tree.ExpressionTree()
    negate_node = nodes.NegateNode(node_tree)
    grp_node = nodes.GroupNode(node_tree, tree.ExpressionTree())
    et.add(negate_node)
    et.add(grp_node)
    assert et.last_value.negate == True

def test_add_negate_node_before_operator(node_tree):
    # not False Or 
    et = tree.ExpressionTree()
    negate_node = nodes.NegateNode(node_tree)
    false_node = nodes.ExpressionLiteralNode(False, node_tree)
    or_node = nodes.OrOperatorNode(node_tree)
    et.add(negate_node)
    et.add(false_node)
    et.add(or_node)

    assert false_node.negate == True
    assert or_node.negate == False
