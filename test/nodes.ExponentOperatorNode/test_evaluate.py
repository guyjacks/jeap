import jeap.tree as node
import jeap.nodes as nodes

def test_evaluate_base(node_tree):
    # 2 ^ 2
    literal_two = nodes.ExpressionLiteralNode(2, node_tree)
    exp_op = nodes.ExponentOperatorNode(node_tree)
    exp_op.left = literal_two
    exp_op.right = literal_two
    assert exp_op.evaluate() == 4
