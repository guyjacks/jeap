import jeap.nodes as nodes
def test_close_pair():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key')
    tree.add(pair_node)

    # only the object node should remain after closing the pair
    tree.close_scope()
    assert 1 == len(tree.json_scope_stack)
    actual_object_node = tree.json_scope_stack[0]
    assert 'object' == actual_object_node.type

def test_close_pair_child():
    tree = nodes.Nodes()

    # test object as pair child
    pair_node = tree.create('pair', 'key')
    object_node = tree.create('object')
    tree.add(pair_node)
    tree.add(object_node)

    # get a handle on the root node before calling close_scope
    expected_root_object_node = tree.json_scope_stack[0]
    tree.close_scope()

    # the scope stack should only contain the root object node that was 
    # created when adding the pair
    assert 1 == len(tree.json_scope_stack)
    assert expected_root_object_node == tree.json_scope_stack[0]

    # test array as pair child
    pair_node = tree.create('pair', 'key')
    array_node = tree.create('array')
    tree.add(pair_node)
    tree.add(array_node)
    tree.close_scope()
    # the scope stack should only contain the root object node that was 
    # created when adding the pair
    assert 1 == len(tree.json_scope_stack)
    assert expected_root_object_node == tree.json_scope_stack[0]

# test closing array nodes

# test closing pair nodes

# test closing text nodes
def test_close_text_node_child_of_pair():
    # closing the text node should close the parent pair node as well
    assert True == False

def test_close_when_scope_stack_empty():
    assert True == False
