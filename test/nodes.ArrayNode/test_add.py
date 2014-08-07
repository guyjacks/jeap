import jeap.tree as tree
import jeap.nodes as nodes

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

def test_add_array_to_pair():
    assert True == False

def test_add_array_to_array():
    assert True == False
