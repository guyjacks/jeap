import jeap.tree as tree
import jeap.nodes as nodes

def test_add_literal_node_base():
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    t.add(array_node)
    value_node = nodes.ValueNode('literal0', tree=t)
    t.add(value_node)

    literal_node_one = nodes.LiteralNode('literal1', t)
    literal_node_two = nodes.LiteralNode('literal2', t)

    t.add(literal_node_one)
    t.add(literal_node_two)
    # the scope should contain 3 nodes; root, array, value
    assert len(t.scope) == 3
    # the value_node should contain 3 childrent LiteralNode 0,1,&2
    # literal_node_one should be the second child of the value_node in scope
    assert t.scope[2].children[1] == literal_node_one
    # literal_node_two should be the third child of the value_node in scope
    assert t.scope[2].children[2] == literal_node_two
