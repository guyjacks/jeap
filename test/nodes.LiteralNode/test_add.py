import jeap.tree as tree
import jeap.nodes as nodes

def test_base():
    t = tree.NodeTree()
    vn = nodes.ValueNode(t)
    ln = nodes.LiteralNode('value', 'string', t)
    vn.add()
    ln.add()

    assert len(t.scope) == 2
    assert t.scope[-1] == vn
    assert ln not in t.scope
    assert vn.children[-1] == ln

def test_add_to_tree_when_parent_is_not_a_value_node()
    assert False
