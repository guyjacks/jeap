import jeap.tree as tree
import jeap.nodes2 as nodes

def test_evaluate_base():
    # 2 + 2
    literal_two = nodes.ExpressionLiteralNode(2)
    add_op = nodes.AddOperatorNode()
    add_op.left = literal_two
    add_op.right = literal_two
    assert add_op.evaluate() == 4
