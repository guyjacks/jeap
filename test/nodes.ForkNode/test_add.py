import test.test_utils as utils
import jeap.nodes as nodes

def test_add_to_empty_tree(node_tree):
    # conditionally adding objects or arrays to the root
    fork_node = nodes.ForkNode(node_tree)
    fork_node.add()

    assert node_tree.root.type == 'root'
    assert node_tree.root.children[0] == fork_node
    assert node_tree.scope[-1] == fork_node
    assert fork_node.root == node_tree.root

def test_add_to_object(node_tree):
    # conditionally adding pairs to an object
    object_node = nodes.ObjectNode(node_tree)
    fork_node = nodes.ForkNode(node_tree)
    object_node.add()
    fork_node.add()

    assert fork_node.root == object_node
    assert object_node.children[0] == fork_node
    assert node_tree.scope[-1] == fork_node

def test_add_to_array(node_tree):
    # conditionally adding items to an array
    array_node = nodes.ArrayNode(node_tree)
    fork_node = nodes.ForkNode(node_tree)
    array_node.add()
    fork_node.add()

    assert fork_node.root == array_node
    assert array_node.children[0] == fork_node
    assert node_tree.scope[-1] == fork_node

def test_add_to_pair(node_tree):
    # conditionally choose a pair value
    utils.add_pair_key_to_tree('key', node_tree)
    pair_node = nodes.PairNode(node_tree)
    fork_node = nodes.ForkNode(node_tree)
    pair_node.add()
    fork_node.add()

    assert fork_node.root == pair_node
    assert pair_node.children[0] == fork_node
    assert node_tree.scope[-1] == fork_node
