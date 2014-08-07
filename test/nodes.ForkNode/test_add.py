import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_empty_tree():
    # conditionally adding objects or arrays to the root
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    fork_node.add()

    assert t.root.type == 'root'
    assert t.root.children[0] == fork_node
    assert t.scope[-1] == fork_node
    assert fork_node.root == t.root

def test_add_to_object():
    # conditionally adding pairs to an object
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    fork_node = nodes.ForkNode(t)
    object_node.add()
    fork_node.add()

    assert fork_node.root == object_node
    assert object_node.children[0] == fork_node
    assert t.scope[-1] == fork_node

def test_add_to_array():
    # conditionally adding items to an array
    t = tree.NodeTree()
    array_node = nodes.ArrayNode(t)
    fork_node = nodes.ForkNode(t)
    array_node.add()
    fork_node.add()

    assert fork_node.root == array_node
    assert array_node.children[0] == fork_node
    assert t.scope[-1] == fork_node

def test_add_to_pair():
    # conditionally choose a pair value
    t = tree.NodeTree()
    key = nodes.ValueNode('key')
    pair_node = nodes.PairNode(key, t)
    fork_node = nodes.ForkNode(t)
    pair_node.add()
    fork_node.add()

    assert fork_node.root == pair_node
    assert pair_node.children[0] == fork_node
    assert t.scope[-1] == fork_node
