import jeap.nodes as nodes

# Test adding pairs
def test_add_pair_to_empty_tree():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key')
    # add a pair as the first tree node
    tree.add(pair_node)

    # the pair node should be the most recent node in the scope stack
    node = tree.json_scope_stack[-1]
    expected = 'key'
    actual = node.key.children[0]
    assert expected == actual

    # an object node should be created and added to the scope stack
    node = tree.json_scope_stack[0]
    expected = 'object'
    actual = node.type
    assert expected == actual

    # the pair node should be the only child of the object node
    actual = node.children[0]
    assert pair_node == actual
    assert 1 == len(node.children)

def test_add_pair_to_object():
    tree = nodes.Nodes()
    object_node = tree.create('object')
    tree.json_scope_stack.append(object_node)
    pair_node = tree.create('pair', 'key')
    tree.add(pair_node)
    
    # the scope stack should ONLY contain the object and the pair
    assert 2 == len(tree.json_scope_stack)
    actual_parent_node = tree.json_scope_stack[0]
    actual_pair_node = tree.json_scope_stack[1]
    assert object_node == actual_parent_node
    assert pair_node == actual_pair_node

    # the pair should be the object's only child
    assert pair_node == actual_parent_node.children[0]
    assert 1 == len(actual_parent_node.children) 

def test_add_pair_to_pair():
    tree = nodes.Nodes()
    object_node = tree.create('object')
    tree.json_scope_stack.append(object_node)
    # this pair node is the current parent
    parent_pair_node = tree.create('pair', 'parent')
    tree.add(parent_pair_node)
    # this pair node is being added while the current parent is a pair
    # in other words, this is a nested pair
    nested_pair_node = tree.create('pair', 'nested')
    tree.add(nested_pair_node)

    # an object should have been created and set as the parent pair's child
    actual_parent_pair = tree.json_scope_stack[1]
    actual_object = actual_parent_pair.children[0]
    assert actual_object.type == 'object'

    # the object should be second to last node in the scope stack
    assert actual_object == tree.json_scope_stack[-2]

    # the nested pair should be the object's only child
    assert nested_pair_node == actual_object.children[0]
    assert 1 == len(actual_object.children)

    # the nested pair should be the current parent
    assert nested_pair_node == tree.json_scope_stack[-1]

def test_add_pair_to_array():
    tree = nodes.Nodes()
    array_node = tree.create('array')
    tree.json_scope_stack.append(array_node)
    print('scope', tree.json_scope_stack)
    pair_node = tree.create('pair', 'key')
    tree.add(pair_node)
    print('scope', tree.json_scope_stack)
    
    # the scope stack should contain only the array, an object, and the 
    # pair.  the reason for the object is that a pair cannot be an array 
    # member.  it must belong to an object
    assert 3 == len(tree.json_scope_stack)
    scope_array_node = tree.json_scope_stack[0]
    scope_object_node = tree.json_scope_stack[1]
    scope_pair_node = tree.json_scope_stack[2]
    assert array_node == scope_array_node
    assert 'object' == scope_object_node.type
    assert pair_node == scope_pair_node

    # the add method should create an object, add the pair to its children,
    # and then add the object to the array's children.

    # the array should have an object as its only child
    assert 'object' == scope_array_node.children[0].type
    assert 1 == len(scope_array_node.children) 

    # the object should contain the pair as its only child
    assert pair_node == scope_object_node.children[0]
    assert 1 == len(scope_object_node.children) 

# Test adding objects
def test_add_object_to_empty_tree():
    tree = nodes.Nodes()
    object_node = tree.create('object')
    tree.add(object_node)
    # the scope stack should contain only the object node
    assert 1 == len(tree.json_scope_stack)
    actual_object_node = tree.json_scope_stack[0]
    assert object_node == actual_object_node

def test_add_object_to_pair():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key') 
    object_node = tree.create('object')
    tree.add(pair_node)
    tree.add(object_node)
    tree.json_scope_stack

    # the scope stack should contain 3 items
    assert 3 == len(tree.json_scope_stack)
    # the first is an object created to hold the pair (not testing this)
    # the second is the pair
    actual_pair_node = tree.json_scope_stack[1]
    # we're not testing this
    # the pair_node's child should be the object
    assert object_node == actual_pair_node.children[0]
    # the last is the new object
    actual_object_node = tree.json_scope_stack[2]
    assert object_node == actual_object_node

def test_add_object_to_array():
    tree = nodes.Nodes()
    array_node = tree.create('array')
    object_node = tree.create('object')
    tree.add(array_node)
    tree.add(object_node)
    # the scope stack should contain 2 nodes
    assert 2 == len(tree.json_scope_stack)
    # the first should be the array (not tested)
    actual_array_node = tree.json_scope_stack[0]
    # the object should be the array's child
    assert object_node == actual_array_node.children[0]
    # the second should be the object
    actual_object_node = tree.json_scope_stack[1]
    assert object_node == actual_object_node

# Test adding arrays
def test_add_array_to_empty_tree():
    tree = nodes.Nodes()
    array_node = tree.create('array')
    tree.add(array_node)
    # the scope stack should only container the array node
    assert 1 == len(tree.json_scope_stack)
    actual_array_node = tree.json_scope_stack[0]
    assert array_node == actual_array_node

def test_add_array_to_pair():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key')
    array_node = tree.create('array')
    tree.add(pair_node)
    tree.add(array_node)
    # the scope stack should contain 3 items
    assert 3 == len(tree.json_scope_stack)
    # the first should be the root object node created to hold the pair
    # we're not testing this
    # the second should be the pair
    # we're not testing this
    actual_pair_node = tree.json_scope_stack[1]
    # the array should be the pair's child
    assert array_node == actual_pair_node.children[0]
    # the array should be the third
    actual_array_node = tree.json_scope_stack[2]
    assert array_node == actual_array_node

def test_add_array_to_array():
    tree = nodes.Nodes()
    root_node = tree.create('array')
    array_node = tree.create('array')
    tree.add(root_node)
    tree.add(array_node)
    # the scope stack should contain 2 nodes
    assert 2 == len(tree.json_scope_stack)
    # the first should be the root node (not testing this)
    # the array should be the child of the root node
    actual_root_node = tree.json_scope_stack[0]
    assert array_node == actual_root_node.children[0]
    # the second should be the array node
    actual_array_node = tree.json_scope_stack[1]
    assert array_node == actual_array_node

# Test adding text nodes
def test_add_text_to_empty_tree():
    # the container must be an array
    tree = nodes.Nodes()
    text_node = tree.create('text', 'value')
    tree.add(text_node)
    # the scope stack should contain 2 nodes
    assert 2 == len(tree.json_scope_stack)
    # the first should be an array node (not testing this)
    # the text node should be a child of the array
    actual_array_node = tree.json_scope_stack[0]
    assert text_node == actual_array_node.children[0]
    # the second should be the text node
    actual_text_node = tree.json_scope_stack[1]
    assert text_node == actual_text_node

def test_add_text_to_pair():
    tree = nodes.Nodes()
    pair_node = tree.create('pair', 'key')
    text_node = tree.create('text', 'text')
    tree.add(pair_node)
    tree.add(text_node)
# the scope stack should contain 3 nodes
    assert 3 == len(tree.json_scope_stack)
    # the first node should be an object (not testing)
    # the second node should be the pair (not testing)
    actual_pair_node = tree.json_scope_stack[1]
    # the text node should be a child of the pair
    assert text_node == actual_pair_node.children[0]
    # the third node should be the text node
    actual_text_node = tree.json_scope_stack[2]
    assert text_node == actual_text_node

def test_add_text_to_array():
    tree = nodes.Nodes()
    array_node = tree.create('array')
    text_node = tree.create('text')
    tree.add(array_node)
    tree.add(text_node)
    # the scope stack should have 2 nodes
    assert 2 == len(tree.json_scope_stack)
    # the first should be the array node (not testing)
    actual_array_node = tree.json_scope_stack[0]
    # the text node should be a child of the array
    assert text_node == actual_array_node.children[0]
    # the second should be the text node
    actual_text_node = tree.json_scope_stack[1]
    assert text_node == actual_text_node

def test_add_text_to_text():
    assert True == False

# Test adding variable nodes
def test_add_variable_to_text():
    assert True == False
