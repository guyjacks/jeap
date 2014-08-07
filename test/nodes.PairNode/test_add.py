import jeap.tree as tree
import jeap.nodes as nodes

def test_add_pair_to_object():
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    t.add(object_node)

    pair_node = nodes.PairNode('key', t)

    t.add(pair_node)
    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].children[0] == pair_node

def test_add_pair_to_empty_tree():
    t = tree.NodeTree()

    pair_node = nodes.PairNode('key')
    pair_node.tree = t

    t.add(pair_node)
    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].type == 'object'
    assert t.scope[1].children[0] == pair_node

def test_add_pair_to_pair():
    assert True == False

def test_add_pair_to_array():
    assert True == False
