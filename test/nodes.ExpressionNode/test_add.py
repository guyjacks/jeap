import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_value(node_tree):
    vn = nodes.ValueNode(node_tree)
    en = nodes.ExpressionNode(node_tree)
    vn.add()
    en.add()

    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == en
    assert vn.children[-1] == en

def test_add_to_fork(node_tree):
    fn = nodes.ForkNode(node_tree)
    en = nodes.ExpressionNode(node_tree)
    fn.add()
    en.add()

    assert len(node_tree.scope) == 4
    assert node_tree.scope[-1] == en
    # adding the expression node to the fork should create a prong node.
    # the prong node's expression should be set to en
    prong_node = fn.children[-1]
    assert prong_node.expression == en
    assert en not in prong_node.children

def test_add_to_empty_tree(node_tree):
    et = tree.ExpressionTree()
    en = nodes.ExpressionNode(node_tree, et)
    en.add()

    # root, value, expression should be in scope
    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == en
    value_node = node_tree.scope[-2]
    assert value_node.children[-1] == en


def test_add_to_pair(node_tree):
    assert False

def test_add_to_array(node_tree):
    assert False

def test_add_to_object(node_tree):
    assert False
