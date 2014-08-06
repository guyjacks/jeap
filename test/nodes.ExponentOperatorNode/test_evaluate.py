import jeap.tree as node
import jeap.nodes2 as nodes

def test_evaluate_base():
    # 2 ^ 2
    literal_two = nodes.ExpressionLiteralNode(2)
    exp_op = nodes.ExponentOperatorNode()
    exp_op.left = literal_two
    exp_op.right = literal_two
    assert exp_op.evaluate() == 4
