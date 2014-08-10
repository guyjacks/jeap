import jeap.nodes as nodes

def test_base(node_tree):
    vn = nodes.ValueNode(node_tree)
    ln = nodes.LiteralNode('value', 'string', node_tree)
    vn.add()
    ln.add()

    assert len(node_tree.scope) == 2
    assert node_tree.scope[-1] == vn
    assert ln not in node_tree.scope
    assert vn.children[-1] == ln

def test_add_to_tree_when_parent_is_not_a_value_node():
    assert False
