import jeap.tree as tree
import jeap.nodes as nodes

def test_add_to_empty_tree():
    t = tree.NodeTree()
    jsn = nodes.JsonStringNode('value', t)
    jsn.add()

    assert len(t.scope) == 2
    assert t.scope[-1].type == 'json_literal_value'
    assert t.scope[-1].children[-1] == jsn
