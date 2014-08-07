import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_empty_tree():
    t = tree.NodeTree()
    branches_node = nodes.BranchesNode(t)
    branches_node.add()

    assert t.root.type == 'root'
    assert t.scope[-1] == branches_node
    assert t.root.children[0] == branches_node
