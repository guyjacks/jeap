import jeap.nodes as nodes

def test_add_object_to_empty_tree(node_tree):
    # add an object when the tree does not have a root node
    object_node = nodes.ObjectNode(node_tree)
    object_node.add()
    # scope should have a root node and an object node
    assert len(node_tree.scope) == 2
    assert node_tree.scope[0].type == 'root'
    assert node_tree.scope[1] == object_node
    # the root node's child should be the object node
    assert node_tree.root.children[0] == object_node

def test_add_to_pair(node_tree):
    assert True == False

def test_add_to_array(node_tree):
    assert True == False

def test_add_to_object(node_tree):
    # an object cannot be added to an object
    assert True == False

def test_add_to_prong(node_tree):
    fork_node = nodes.ForkNode(node_tree)
    prong_node = nodes.ProngNode(node_tree)
    object_node = nodes.ObjectNode(node_tree)
    fork_node.add()
    prong_node.add()
    object_node.add()

    assert prong_node.children[-1] == object_node
    assert len(node_tree.scope) == 4
    assert node_tree.scope[-1] == object_node
    assert object_node not in node_tree.root.children

def test_add_to_prong_when_prong_root_is_object(node_tree):
    # an object cannot be added to an object
    assert True == False
