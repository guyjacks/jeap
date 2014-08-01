import jeap.tree as tree
import jeap.nodes2 as nodes

def test_base():
    t = tree.NodeTree()
    node = nodes.PairNode('key', t)
    t.add(node)
    assert t.get_scoped_node() is node
    assert t.get_scoped_node(1) is node
    assert t.get_scoped_node(2).type == 'object'
    assert t.get_scoped_node(3).type == 'root'
