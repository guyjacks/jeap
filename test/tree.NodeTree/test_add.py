import jeap.tree as tree
import jeap.nodes2 as nodes

def test_add_root_node_base():
    t = tree.NodeTree()
    root_node = nodes.RootNode(t)

    root_node.add()
    assert t.root == root_node
    assert len(t.scope) == 1
    assert t.scope[0] == root_node

def test_add_object_node_to_empty_tree():
    # add an object when the tree does not have a root node
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    t.add(object_node)
    # scope should have a root node and an object node
    assert len(t.scope) == 2
    assert t.scope[0].type == 'root'
    assert t.scope[1] == object_node
    # the root node's child should be the object node
    assert t.root.children[0] == object_node

def test_add_array_node_to_empty_tree():
    # add the array when the tree does not contain a root node
    t = tree.NodeTree()

    array_node = nodes.ArrayNode(t)
    
    t.add(array_node)
    # scope should contain root node and an array node
    assert len(t.scope) == 2
    assert t.scope[1] == array_node
    assert t.scope[0].type == 'root'
    # the root nodes' child should be the array node
    assert t.root.children[0] == array_node

def test_add_pair_node_to_object():
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    t.add(object_node)

    pair_node = nodes.PairNode('key', t)

    t.add(pair_node)
    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].children[0] == pair_node

def test_add_pair_node_without_object():
    t = tree.NodeTree()

    pair_node = nodes.PairNode('key')
    pair_node.tree = t

    t.add(pair_node)
    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].type == 'object'
    assert t.scope[1].children[0] == pair_node

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
