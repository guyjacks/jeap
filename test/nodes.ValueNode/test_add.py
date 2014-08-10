import jeap.nodes as nodes
import test.test_utils as utils

def test_add_to_empty_tree(node_tree):
    lvn = nodes.ValueNode(node_tree)
    lvn.add()

    assert node_tree.root.type == 'root'
    assert len(node_tree.scope) == 2
    assert node_tree.scope[-1] == lvn

def test_add_to_pair(node_tree):
    pair_key_node = utils.add_pair_key_to_tree('key', node_tree)
    pair_node = nodes.PairNode(node_tree)
    lvn = nodes.ValueNode(node_tree)
    pair_node.add()
    lvn.add()

    assert len(node_tree.scope) == 4
    assert node_tree.scope[-1] == lvn
    assert pair_node.key == pair_key_node
    assert pair_node.children[-1] == lvn

def test_add_to_array(node_tree):
    array_node = nodes.ArrayNode(node_tree)
    lvn = nodes.ValueNode(node_tree)
    array_node.add()
    lvn.add()

    assert array_node.children[-1] == lvn
    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == lvn

def test_add_to_object(node_tree):
    on = nodes.ObjectNode(node_tree)
    vn = nodes.ValueNode(node_tree)
    on.add()
    vn.add()

    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == vn
    assert vn not in on.children

def test_add_to_prong(node_tree):
    fn = nodes.ForkNode(node_tree)
    pn = nodes.ProngNode(node_tree)
    vn = nodes.ValueNode(node_tree)
    fn.add()
    pn.add()
    vn.add()

    print('pn.root', pn.root)

    assert len(node_tree.scope) == 4
    assert node_tree.scope[-1] == vn
    assert vn not in pn.children
