import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    # 2 + 2 * 4^2 / 2 - 1
    et = tree.ExpressionTree()
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    literal_four = nodes.ExpressionLiteralNode(4, node_tree)
    literal_one = nodes.ExpressionLiteralNode(1, node_tree)
    aon = nodes.AddOperatorNode(node_tree)
    mon = nodes.MultiplyOperatorNode(node_tree)
    eon = nodes.ExponentOperatorNode(node_tree)
    don = nodes.DivideOperatorNode(node_tree)
    son = nodes.SubtractOperatorNode(node_tree)
    et.add(literal_two)
    et.add(aon)
    et.add(literal_two)
    et.add(mon)
    et.add(literal_four)
    et.add(eon)
    et.add(literal_two)
    et.add(don)
    et.add(literal_two)
    et.add(son)
    et.add(literal_one)
    et.close()
    assert et.evaluate() == 17
