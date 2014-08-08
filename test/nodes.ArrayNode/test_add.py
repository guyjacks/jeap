import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_empty_tree():
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

def test_add_to_pair():
    assert True == False

def test_add_to_array():
    assert True == False

def test_add_to_prong():
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    prong_node = nodes.ProngNode(t)
    array_node = nodes.ArrayNode(t)
    fork_node.add()
    prong_node.add()
    array_node.add()

    assert len(t.scope) == 4
    assert t.scope[-1] == array_node
    assert prong_node.children[-1] == array_node
    assert array_node not in t.root.children

def test_add_to_prong_when_prong_root_is_object():
    # an array cannot be added to an object
    assert True == False
