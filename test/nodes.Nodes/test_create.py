import jeap.nodes as nodes
def test_create_pair_node():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key')
    assert 'pair' == pair_node.type

    # the key should be a TextNode which stores its values in its 
    # children list
    actual = pair_node.key.children[0]
    assert 'key' == pair_node.key.children[0]

def test_create_object_node():
    tree = nodes.Nodes()
    object_node = tree.create('object')
    assert 'object' == object_node.type

def test_create_array_node():
    tree = nodes.Nodes()
    array_node = tree.create('array')
    assert 'array' == array_node.type

def test_create_text_node():
    tree = nodes.Nodes()
    text_node = tree.create('text', 'value')
    assert 'text' == text_node.type
    assert 'value' == text_node.children[0]
