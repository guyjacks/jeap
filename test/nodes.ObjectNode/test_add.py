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

def test_add_object_to_pair():
    assert True == False

def test_add_object_to_array():
    assert True == False
