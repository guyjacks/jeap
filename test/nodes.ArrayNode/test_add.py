import jeap.nodes as nodes

def test_add_to_empty_tree(node_tree):
    array_node = nodes.ArrayNode(node_tree)
    array_node.add()
    
    # scope should contain root node and an array node
    assert len(node_tree.scope) == 2
    assert node_tree.scope[1] == array_node
    assert node_tree.scope[0].type == 'root'
    # the root nodes' child should be the array node
    assert node_tree.root.children[0] == array_node

def test_add_to_pair():
    assert True == False

def test_add_to_array():
    assert True == False

def test_add_to_prong(node_tree):
    fork_node = nodes.ForkNode(node_tree)
    prong_node = nodes.ProngNode(node_tree)
    array_node = nodes.ArrayNode(node_tree)
    fork_node.add()
    prong_node.add()
    array_node.add()

    assert len(node_tree.scope) == 4
    assert node_tree.scope[-1] == array_node
    assert prong_node.children[-1] == array_node
    assert array_node not in node_tree.root.children

def test_add_to_prong_when_prong_root_is_object():
    # an array cannot be added to an object
    assert True == False
