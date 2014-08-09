import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_value():
    t = tree.NodeTree()
    vn = nodes.ValueNode(t)
    en = nodes.ExpressionNode(t)
    vn.add()
    en.add()

    assert len(t.scope) == 3
    assert t.scope[-1] == en
    assert vn.children[-1] == en

def test_add_to_fork():
    t = tree.NodeTree()
    fn = nodes.ForkNode(t)
    en = nodes.ExpressionNode(t)
    fn.add()
    en.add()

    assert len(t.scope) == 4
    assert t.scope[-1] == en
    # adding the expression node to the fork should create a prong node.
    # the prong node's expression should be set to en
    prong_node = fn.children[-1]
    assert prong_node.expression == en
    assert en not in prong_node.children

def test_add_to_array():
    assert False

def test_add_to_object():
    assert False

def test_add_to_empty_tree():
    assert False

def test_add_to_pair():
    assert False
