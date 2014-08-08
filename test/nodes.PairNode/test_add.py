import jeap.tree as tree
import jeap.nodes as nodes

def add_pair_key_to_tree(key, tree):
    pair_key_value_node = nodes.JsonLiteralValueNode(tree)
    pair_key_literal_node = nodes.JsonStringNode(key, tree)
    pair_key_value_node.add()
    pair_key_literal_node.add()
    return pair_key_value_node

def test_pair_key_is_set_to_parent_value_node():
    t = tree.NodeTree()
    pair_key_node = add_pair_key_to_tree('key', t)
    pair_node = nodes.PairNode(t)
    pair_node.add()

    assert pair_node.key == pair_key_node
    assert pair_key_node not in t.scope
    assert pair_key_node.children[0].value == 'key'

def test_add_to_object():
    t = tree.NodeTree()
    object_node = nodes.ObjectNode(t)
    object_node.add()

    add_pair_key_to_tree('key', t)
    pair_node = nodes.PairNode(t)
    pair_node.add()

    assert len(t.scope) == 3
    assert t.scope[-1] == pair_node
    assert t.scope[-2].children[-1] == pair_node

def test_add_to_empty_tree():
    t = tree.NodeTree()
    add_pair_key_to_tree('key', t)
    pair_node = nodes.PairNode(t)
    pair_node.add()

    assert len(t.scope) == 3
    assert t.scope[-1] == pair_node
    assert t.scope[-2].type == 'object'
    assert t.scope[-2].children[-1] == pair_node

def test_add_to_pair():
    assert False

def test_add_to_array():
    assert False

def test_add_to_prong():
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    prong_node = nodes.ProngNode(t)
    pair_node = nodes.PairNode(t)
    fork_node.add()
    prong_node.add()
    add_pair_key_to_tree('key', t)
    pair_node.add()

    assert prong_node.children[-1].type == 'object'
    # should be child of object implicitly created by pair_node.add()
    assert prong_node.children[-1].children[-1] == pair_node
    assert len(t.scope) == 5
    assert t.scope[-1] == pair_node
