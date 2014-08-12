import jeap.tree as tree
import jeap.nodes as nodes

def test_arithmetic_operators(node_tree):
    # 1 + (2 - 3) * 4 / 5 ^ 6
    et = tree.ExpressionTree()
    gn = nodes.GroupNode(node_tree, tree.ExpressionTree())
    one = nodes.ExpressionLiteralNode(1, node_tree)
    two = nodes.ExpressionLiteralNode(2, node_tree)
    three = nodes.ExpressionLiteralNode(3, node_tree)
    four = nodes.ExpressionLiteralNode(4, node_tree)
    five = nodes.ExpressionLiteralNode(5, node_tree)
    six = nodes.ExpressionLiteralNode(6, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    son = nodes.SubtractOperatorNode(node_tree)
    mon = nodes.MultiplyOperatorNode(node_tree)
    don = nodes.DivideOperatorNode(node_tree)
    eon = nodes.ExponentOperatorNode(node_tree)
    et.add(one)
    et.add(aon)
    et.add(gn)
    et.add(two)
    et.add(son)
    et.add(three)
    et.close()
    et.add(mon)
    et.add(four)
    et.add(don)
    et.add(five)
    et.add(eon)
    et.add(six)
    et.close()
    assert str(et) == '1 + (2 - 3) * 4 / 5 ^ 6'

def test_print_expression_with_variables(node_tree):
    assert False

def test_boolean_operators(node_tree):
    # not True or False and not (True and False)
    et = tree.ExpressionTree()
    gn = nodes.GroupNode(node_tree, tree.ExpressionTree())
    nn = nodes.NegateNode(node_tree)
    tn_one = nodes.ExpressionLiteralNode(True, node_tree)
    tn_two = nodes.ExpressionLiteralNode(True, node_tree)
    fn_one = nodes.ExpressionLiteralNode(False, node_tree)
    fn_two = nodes.ExpressionLiteralNode(False, node_tree)
    oon = nodes.OrOperatorNode(node_tree)
    aon_one = nodes.AndOperatorNode(node_tree)
    aon_two = nodes.AndOperatorNode(node_tree)
    et.add(nn)
    et.add(tn_one)
    et.add(oon)
    et.add(fn_one)
    et.add(aon_one)
    et.add(nn)
    et.add(gn)
    et.add(tn_two)
    et.add(aon_two)
    et.add(fn_two)
    et.close()
    et.close()
    print(et)
    assert str(et) == 'not True or False and not (True and False)'
