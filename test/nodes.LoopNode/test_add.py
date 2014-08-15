import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    ln = nodes.LoopNode(node_tree)
    ln.add()
    assert len(node_tree.scope) == 2
    assert node_tree.scope[-1] == ln
    assert ln.root.type == 'root'

def test_add_to_array(node_tree):
    an = nodes.ArrayNode(node_tree)
    ln = nodes.LoopNode(node_tree)
    an.add()
    ln.add()
    assert len(node_tree.scope) == 3
    assert node_tree.scope[-1] == ln
    assert ln.root == an
