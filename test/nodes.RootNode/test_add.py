import jeap.tree as tree
import jeap.nodes as nodes

def test_base():
    t = tree.NodeTree()
    root_node = nodes.RootNode(t)

    root_node.add()
    assert t.root == root_node
    assert len(t.scope) == 1
    assert t.scope[0] == root_node
