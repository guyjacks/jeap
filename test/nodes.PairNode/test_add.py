import test.test_utils as utils
import jeap.nodes as nodes

def test_pair_key_is_set_to_parent_value_node(node_tree):
    pair_key_node = utils.add_pair_key_to_tree('key', node_tree)
    pair_node = nodes.PairNode(node_tree)
    pair_node.add()

    assert pair_node.key == pair_key_node
    assert pair_key_node not in node_tree.scope
    assert pair_key_node.children[0].value == 'key'

def test_add_to_object(node_tree):
    object_node = nodes.ObjectNode(node_tree)
    object_node.add()

    pair_key_node = utils.add_pair_key_to_tree('key', node_tree)
    pair_node = nodes.PairNode(node_tree)
    pair_node.add()

    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == pair_node
    assert node_tree.scope[-2].children[-1] == pair_node

def test_add_to_empty_tree(node_tree):
    utils.add_pair_key_to_tree('key', node_tree)
    pair_node = nodes.PairNode(node_tree)
    pair_node.add()

    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == pair_node
    assert node_tree.scope[-2].type == 'object'
    assert node_tree.scope[-2].children[-1] == pair_node

def test_add_to_pair():
    assert False

def test_add_to_array():
    assert False

def test_add_to_prong(node_tree):
    fork_node = nodes.ForkNode(node_tree)
    prong_node = nodes.ProngNode(node_tree)
    pair_node = nodes.PairNode(node_tree)
    fork_node.add()
    prong_node.add()
    utils.add_pair_key_to_tree('key', node_tree)
    pair_node.add()

    assert prong_node.children[-1].type == 'object'
    # should be child of object implicitly created by pair_node.add()
    assert prong_node.children[-1].children[-1] == pair_node
    assert len(node_tree.scope) == 5
    assert node_tree.scope[-1] == pair_node
