import jeap.tree as tree
import jeap.nodes as nodes

def test_add_symbol_node_base():
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    t.add(array_node)
    value_node = nodes.ValueNode('literal0', tree=t)
    t.add(value_node)

    symbol_node_one = nodes.SymbolNode('a', t)
    symbol_node_two = nodes.SymbolNode('b', t)

    t.add(symbol_node_one)
    t.add(symbol_node_two)
    # the scope should contain 3 nodes; root, array, value
    assert len(t.scope) == 3
    # the value_node should contain 3 children; a literal node, 
    # symbol_node_one, and symbol_node_two
    # symbol_node_one should be the second child of the value_node in scope
    assert t.scope[2].children[1] == symbol_node_one
    # symbol_node_two should be the third child of the value_node in scope
    assert t.scope[2].children[2] == symbol_node_two
