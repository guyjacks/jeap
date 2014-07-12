import jeap.tree as tree
import jeap.nodes2 as nodes

def test_base():
    t = tree.NodeTree()

    node = nodes.ObjectNode()
    t.add_to_scope(node)
    assert t.scope[0] is node

    t.remove_from_scope()
    assert 0 == len(t.scope)
