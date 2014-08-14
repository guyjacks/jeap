import jeap.tree as tree
import jeap.nodes as nodes

def add_pair_key_to_tree(key, tree):
    pair_key_value_node = nodes.ValueNode(tree)
    pair_key_literal_node = nodes.LiteralNode(key, 'string', tree)
    pair_key_value_node.add()
    pair_key_literal_node.add()
    return pair_key_value_node

# create objects to test context variables and accessors
class ObjectX(object):
    def __init__(self):
        self.y = {'key': ObjectC()}

class ObjectC(object):
    def __init__(self):
        self.a = ['a', 'b', 'c']


