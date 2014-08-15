import jeap.tree as tree
import jeap.nodes as nodes

def test_base(node_tree):
    ln = nodes.LoopNode(node_tree)
    lin_key = nodes.LoopIdentifierNode('k', 'key', node_tree)
    lin_value = nodes.LoopIdentifierNode('v', 'value', node_tree)
    ln.add()
    lin_key.add()
    lin_value.add()
    assert ln.key_identifier == lin_key
    assert ln.value_identifier == lin_value
