import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_object():
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    pair_node = nodes.PairNode('key', t)
    object_node.add()
    pair_node.add()

    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].children[0] == pair_node

def test_add_to_empty_tree():
    t = tree.NodeTree()
    pair_node = nodes.PairNode('key', t)
    pair_node.add()

    assert len(t.scope) == 3
    assert t.scope[2] == pair_node
    assert t.scope[1].type == 'object'
    assert t.scope[1].children[0] == pair_node

def test_add_to_pair():
    assert True == False

def test_add_to_array():
    assert True == False

def test_add_to_prong():
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    prong_node = nodes.ProngNode(t)
    pair_node = nodes.PairNode('key', t)
    fork_node.add()
    prong_node.add()
    pair_node.add()

    assert prong_node.children[0].type == 'object'
    # should be child of object implicitly created by pair_node.add()
    assert prong_node.children[0].children[0] == pair_node
    assert len(t.scope) == 5
    assert t.scope[-1] == pair_node
