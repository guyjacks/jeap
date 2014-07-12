import jeap.nodes2 as nodes
import jeap.tree as tree

def test_factory():
    t = tree.NodeTree()

    node = nodes.Node(t)
    assert None is node.type

    value_node = node.factory('value', 'value')
    assert 'value' == value_node.type

    literal_node = node.factory('literal', 'value')
    assert 'literal' == literal_node.type

    symbol_node = node.factory('symbol', 'identifier')
    assert 'symbol' == symbol_node.type

    pair_node = node.factory('pair', 'key')
    assert 'pair' == pair_node.type

    object_node = node.factory('object')
    assert 'object' == object_node.type

    array_node = node.factory('array', 'value')
    assert 'array' == array_node.type

    root_node = node.factory('root', 'value')
    assert 'root' == root_node.type
