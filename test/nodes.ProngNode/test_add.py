import jeap.nodes as nodes

def test_base(node_tree):
    fork_node = nodes.ForkNode(node_tree)
    prong_node = nodes.ProngNode(node_tree)
    fork_node.add()
    prong_node.add()

    assert prong_node.root == fork_node.root
    assert fork_node.children[0] == prong_node
    assert node_tree.scope[-1] == prong_node
