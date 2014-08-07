import jeap.tree as tree
import jeap.nodes as nodes

def test_add_object_to_empty_tree():
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

def test_add_to_pair():
    assert True == False

def test_add_to_array():
    assert True == False

def test_add_to_object():
    # an object cannot be added to an object
    assert True == False

def test_add_to_prong():
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    prong_node = nodes.ProngNode(t)
    object_node = nodes.ObjectNode(t)
    fork_node.add()
    prong_node.add()
    object_node.add()

    assert prong_node.children[-1] == object_node
    assert len(t.scope) == 4
    assert t.scope[-1] == object_node
    assert object_node not in t.root.children

def test_add_to_prong_when_prong_root_is_object():
    # an object cannot be added to an object
    assert True == False
