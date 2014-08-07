import jeap.tree as tree
import jeap.nodes as nodes

def test_add_value_node_to_pair():
    t = tree.NodeTree()

    pair_node = nodes.PairNode('key', t)
    t.add(pair_node)
    
    value_node = nodes.ValueNode('value', tree=t)

    t.add(value_node)
    # scope stack should contain 4 nodes; root, object, pair, and value
    assert len(t.scope) == 4
    # pair node's first child should be the value_node
    assert t.scope[2].children[0] == value_node
    # the value node should be added to the scope
    assert t.scope[3] == value_node
    
def test_add_value_node_to_array():
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    t.add(array_node)

    value_node = nodes.ValueNode('value', tree=t)

    t.add(value_node)
    # scope stack should contain 3 nodes; root, array, and value
    assert len(t.scope) == 3
    # array node's first child should be the value_node
    assert t.scope[1].children[0] == value_node
    # the value node should be added to the scope
    assert t.scope[2] == value_node
 
