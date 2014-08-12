import jeap.tree as tree
import jeap.nodes as nodes

def test_number(node_tree):
    eln = nodes.ExpressionLiteralNode(2.2, node_tree)
    assert eln.evaluate() == 2.2

def test_boolean(node_tree):
    eln = nodes.ExpressionLiteralNode(False, node_tree)
    assert eln.evaluate() == False

    eln = nodes.ExpressionLiteralNode(True, node_tree)
    assert eln.evaluate() == True
    
def test_negate_boolean(node_tree):
    eln = nodes.ExpressionLiteralNode(False, node_tree)
    eln.negate = True
    assert eln.evaluate() == True

    eln = nodes.ExpressionLiteralNode(True, node_tree)
    eln.negate = True
    assert eln.evaluate() == False

def test_string(node_tree):
    eln = nodes.ExpressionLiteralNode('hello world', node_tree)
    assert eln.evaluate() == 'hello world'

def test_list(node_tree):
    eln = nodes.ExpressionLiteralNode([1, 2, 3], node_tree)
    assert eln.evaluate() == [1, 2, 3]

def test_dict(node_tree):
    d = {'first': 'Guy', 'middle': 'l', 'last': 'jacks'}
    eln = nodes.ExpressionLiteralNode(d, node_tree)
    assert eln.evaluate() == d
