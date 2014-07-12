class NodeFactory(object):
    def __init__(self):
        self.tree = None

    def create(self, type, *args, **kwargs):
        value = args[0] if len(args) > 0 else None
        if type == 'value':
            return ValueNode(tree, value)
        elif type == 'literal':
            return LiteralNode(tree, value)
        elif type == 'symbol':
            return SymbolNode(tree, value)
        elif type == 'pair':
            key = self.factory('value', value)
            return PairNode(key, tree)
        elif type == 'object':
            return ObjectNode(tree)
        elif type == 'array':
            return ArrayNode(tree)
        elif type == 'root':
            return RootNode(tree)

class Node(object):
# ATTENTION: compiler will create a tree and then set it as the value for 
# Node.tree.  This way, all intances have access to it
# ast = NodeTree()
# Node.tree = ast
    def __init__(self, tree = None):
        self.type = None
        self.children = []
        self.tree = tree

    def factory(self, type, *args, **kwargs):
        value = args[0] if len(args) > 0 else None
        if type == 'value':
            return ValueNode(value)
        elif type == 'literal':
            return LiteralNode(value)
        elif type == 'symbol':
            return SymbolNode(value)
        elif type == 'pair':
            key = self.factory('value', value)
            return PairNode(key)
        elif type == 'object':
            return ObjectNode()
        elif type == 'array':
            return ArrayNode()
        elif type == 'root':
            return RootNode()

    def on_enter_scope(self, current_parent):
        pass

    def on_add(self):
        # execute whenever this node is added to an AST
        pass

    def on_exit_scope(self):
        self.tree.remove_from_scope()

    def on_child_exits_scope(self, child_node):
        # called when a child is closed
        pass

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        pass

    def render_children(self):
        pass

class RootNode(Node):
    def __init__(self, tree = None):
        super(RootNode, self).__init__(tree)
        self.type = 'root'

    def on_add(self, parent_node):
        self.tree.root = self
        self.tree.add_to_scope(self)

class ObjectNode(Node):
    def __init__(self, tree = None):
        super(ObjectNode, self).__init__(tree)
        self.type = 'object'

    def on_add(self, parent_node):
        if parent_node is None:
            new_root_node = RootNode(self.tree)
            self.tree.add(new_root_node)
            self.tree.add(self)
        elif parent_node.type in ('pair', 'array', 'root'):
            parent_node.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise error
            pass

    def add_child(self, node):
        #This is where we detect a pair has been added with a key matching the key of a pair contained by the object in scope.  We must close the current object's scope and then create a new dictionary.
        super(ObjectNode, self).add_child(node)

class ArrayNode(Node):
    def __init__(self, tree = None):
        super(ArrayNode, self).__init__(tree)
        self.type = 'array'

    def on_add(self, parent_node):
        if parent_node is None:
            new_root_node = RootNode(self.tree)
            self.tree.add(new_root_node)
            self.tree.add(self)
        elif parent_node.type in ('pair', 'array', 'root'):
            parent_node.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise error
            pass

class PairNode(Node):
    def __init__(self, key, tree = None):
        """
            @key: must be a ValueNode
        """
        super(PairNode, self).__init__(tree)
        self.type = 'pair'
        self.key = key

    def on_add(self, parent_node):
# a pair must always be the child of an object
        if (parent_node is None) or (parent_node.type != 'object'):
            new_object_node = ObjectNode(self.tree)
#new_object_node.add_child(self)
            self.tree.add(new_object_node)
            self.tree.add(self)
        else:
            parent_node.add_child(self)
            self.tree.add_to_scope(self)

    def on_child_exits_scope(self, child_node):
# A pair's children can only contain a single node.  The child node's type 
# must be an object, an array, or a value node.  It CANNOT be
# another pair because a pair can only exist as the child of an object.
        self.tree.close_scope()

class ValueNode(Node):
# ATTENTION: json.org specifies that a pair key must be a string so
# its possible that I will need to create a separate type for pair key.
    def __init__(self, value, symbol = False, tree = None):
        super(ValueNode, self).__init__(tree)
        self.type = 'value'
        if symbol == True:
            self.add_child(SymbolNode(value, self.tree))
        else:
            self.add_child(LiteralNode(value, self.tree))

    def on_add(self, parent_node):
        if parent_node.type in ('array', 'pair'):
            parent_node.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise error
            pass

    def render(self):
        # ex. children = [LiteralNode('hello'), SymbolNode('name'), LiteralNode('35'), ...]
        # loop through children
            # link variables to value and concatenate children
        # the compiler will supply a link() function that returns an error
        # or the variables value
        # the link function looks up the variable name in the compilers symbol table
        pass

class SymbolNode(Node):
    def __init__(self, identifier, tree = None):
        super(SymbolNode, self).__init__(tree)
        self.type = 'symbol'
        self.identifier = identifier

    def on_add(self, parent_node):
        if parent_node.type == 'value':
            parent_node.add_child(self)
        else:
            # raise error
            pass

    def render(self, symbol_table):
        return symbol_table[self.identifier]

class LiteralNode(Node):
    def __init__(self, value, tree = None):
        super(LiteralNode, self).__init__(tree)
        self.type = 'literal'
        self.value = value

    def on_add(self, parent_node):
        if parent_node.type == 'value':
            parent_node.add_child(self)
        else:
            # raise error
            pass

    def render(self):
        return self.value

#### Flow Control Nodes ####

class ExpressionNode(object):
    def __init__(self, expression):
        pass
    def evaluate():
        pass

class LoopNode(object):
    def __init__(self, expression):
        pass

class IfNode(object):
    def __init__(self, expression):
        pass
