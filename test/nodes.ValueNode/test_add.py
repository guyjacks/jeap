import jeap.tree as tree
import jeap.nodes as nodes
import test.test_utils as utils

def test_add_to_empty_tree():
    t = tree.NodeTree()
    lvn = nodes.ValueNode(t)
    lvn.add()

    assert t.root.type == 'root'
    assert len(t.scope) == 2
    assert t.scope[-1] == lvn

def test_add_to_pair():
    t = tree.NodeTree()
    pair_key_node = utils.add_pair_key_to_tree('key', t)
    pair_node = nodes.PairNode(t)
    lvn = nodes.ValueNode(t)
    pair_node.add()
    lvn.add()

    assert len(t.scope) == 4
    assert t.scope[-1] == lvn
    assert pair_node.key == pair_key_node
    assert pair_node.children[-1] == lvn

def test_add_to_array():
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    lvn = nodes.ValueNode(t)
    array_node.add()
    lvn.add()

    assert array_node.children[-1] == lvn
    assert len(t.scope) == 3
    assert t.scope[-1] == lvn

def test_add_to_object():
    t = tree.NodeTree()
    on = nodes.ObjectNode(t)
    vn = nodes.ValueNode(t)
    on.add()
    vn.add()

    assert len(t.scope) == 3
    assert t.scope[-1] == vn
    assert vn not in on.children

def test_add_to_prong():
    t = tree.NodeTree()
    fn = nodes.ForkNode(t)
    pn = nodes.ProngNode(t)
    vn = nodes.ValueNode(t)
    fn.add()
    pn.add()
    vn.add()

    print('pn.root', pn.root)

    assert len(t.scope) == 4
    assert t.scope[-1] == vn
    assert vn not in pn.children
