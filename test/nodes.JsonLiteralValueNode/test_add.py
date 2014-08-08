import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_empty_tree():
    t = tree.NodeTree()
    lvn = nodes.JsonLiteralValueNode(t)
    lvn.add()

    assert t.root.type == 'root'
    assert len(t.scope) == 2
    assert t.scope[-1] == lvn

def test_add_to_pair():
    assert False

def test_add_to_array():
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    lvn = nodes.JsonLiteralValueNode(t)
    array_node.add()
    lvn.add()

    assert array_node.children[-1] == lvn
    assert len(t.scope) == 3
    assert t.scope[-1] == lvn
