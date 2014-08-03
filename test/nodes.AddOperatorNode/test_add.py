import jeap.tree as tree
import jeap.nodes2 as nodes

def test_add_as_first_operator():
    t = tree.NodeTree() 
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(t, et)
    literal_node = nodes.ExpressionLiteralNode(2, et)
    et.add(literal_node)
    add_op = nodes.AddOperatorNode(et)
    et.add(add_op)
    assert et.last_operator == add_op
    assert add_op.left == literal_node
