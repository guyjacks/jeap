import jeap.tree as tree
import jeap.nodes as nodes

def test_base():
    t = tree.NodeTree()
    fork_node = nodes.ForkNode(t)
    prong_node = nodes.ProngNode(t)
    fork_node.add()
    prong_node.add()

    assert prong_node.root == fork_node.root
    assert fork_node.children[0] == prong_node
    assert t.scope[-1] == prong_node
