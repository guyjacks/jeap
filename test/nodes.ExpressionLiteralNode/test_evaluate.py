import jeap.tree as tree
import jeap.nodes as nodes

def test_number():
    eln = nodes.ExpressionLiteralNode(2.2)
    assert eln.evaluate() == 2.2

def test_boolean():
    eln = nodes.ExpressionLiteralNode(False)
    assert eln.evaluate() == False

    eln = nodes.ExpressionLiteralNode(True)
    assert eln.evaluate() == True
    
def test_negate_boolean():
    eln = nodes.ExpressionLiteralNode(False)
    eln.negate = True
    assert eln.evaluate() == True

    eln = nodes.ExpressionLiteralNode(True)
    eln.negate = True
    assert eln.evaluate() == False

def test_string():
    eln = nodes.ExpressionLiteralNode('hello world')
    assert eln.evaluate() == 'hello world'

def test_list():
    eln = nodes.ExpressionLiteralNode([1, 2, 3])
    assert eln.evaluate() == [1, 2, 3]

def test_dict():
    d = {'first': 'Guy', 'middle': 'l', 'last': 'jacks'}
    eln = nodes.ExpressionLiteralNode(d)
    assert eln.evaluate() == d
