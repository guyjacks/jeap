import jeap.tree as tree
import jeap.nodes as nodes

def test_add_loop_cycle_context_identifier_node(node_tree):
    ln = nodes.LoopNode(node_tree)
    lin_key = nodes.LoopIdentifierNode('k', 'key', node_tree)
    lin_value = nodes.LoopIdentifierNode('v', 'value', node_tree)
    ln.add_child(lin_key)
    ln.add_child(lin_value)
    assert ln.key_identifier == lin_key
    assert ln.value_identifier == lin_value

def test_add_expression_to_statement(node_tree):
    ln = nodes.LoopNode(node_tree)
    en = nodes.ExpressionNode(node_tree, tree.ExpressionTree())
    ln.add_child(en)
    assert ln.iterable == en
    
def test_add_non_statement_node(node_tree):
    ln = nodes.LoopNode(node_tree)
    on = nodes.ObjectNode(node_tree)
    ln.statement_open = False
    ln.add_child(on)
    assert ln.children[-1] == on
