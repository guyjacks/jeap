class Nodes(object):
    def __init__(self):
        # track scope for json objects
        #self.json_nest_level = 0

        self.current_token_value = Null
        # Code Mentor - should this be an object variable or class variable
        self.json_scope_stack = []

        # track scope once inside a block
        # self.block_nest_level = 0
        # self.block_scope_stack = []

    def create(self, type, value=""):
        if type == 'text':
            return TextNode(value)
        elif type == 'variable':
            return TextNode(value, True)
        elif type == 'pair':
            # create a text node to hold the key
            key = self.create('text', value)
            return PairNode(key)
        elif type == 'object':
            return ObjectNode()
        elif type == 'array':
            return ArrayNode()

    def add(self, node):
        if node.type == 'pair':
            self.__add_pair_node(node)
        elif node.type == 'object':
            self.__add_object_node(node)
        elif node.type == 'array':
            self.__add_array_node(node)
        elif node.type == 'text':
            self.__add_text_node(node)

    def close_scope(self):
        """
        close events
        - general
          - dedent
          - end of input/file
        - containers only (arr or object)
          - explicit close ']' or '}'
        - pairs only
          - close if value is closed (nested container)
        """
        # close the current item in scope by removing it from the scope 
        # stack
        self.json_scope_stack.pop()

        # A pair can only have one child so if its child is closed then 
        # it also must be closed
        parent = self.__parent()
        if parent.type == 'pair':
            self.json_scope_stack.pop()
            
    def __parent(self):
        if len(self.json_scope_stack) > 0:
            return self.json_scope_stack[-1]
        else:
            # this is the root node
            return False

    def __add_pair_node(self, pair_node):
        parent = self.__parent()
        if parent:
            # a pair's value must be an object, an array, or text.
            if parent.type == 'pair':
                # a nested pair indicates the parent pair node's value 
                # is an object
                # since the object is not explicitly stated, we must 
                # create it.  It's first child is this pair.
                object_node = ObjectNode()
                object_node.add_child(pair_node)
                # the object is value of the parent pair node so we add
                # it to the parent's children
                parent.add_child(object_node)
                # the new object will become the parent after the new 
                # pair node is closed.  the next pair node (if there 
                # is one) will be a child of this object.
                self.json_scope_stack.append(object_node)
                # the new pair node will be become the current parent.
                # if the next node will be the value of this pair node
                self.json_scope_stack.append(pair_node)
            elif parent.type == 'object':
                parent.add_child(pair_node)
                self.json_scope_stack.append(pair_node)
            elif parent.type == 'array':
                object_node = self.create('object')
                object_node.add_child(pair_node)
                parent.add_child(object_node)
                self.json_scope_stack.append(object_node)
                self.json_scope_stack.append(pair_node)
        else:
            # No parent indicates this node is the first to be added.
            # We must create a root node of which all other nodes will be 
            # descendants.  The root node must be an array or object.
            # pair nodes can only be children of objects so the root
            # must be an object.  We must create the root node and add 
            # this pair node as its first child.
            root_node = self.create('object')
            root_node.add_child(pair_node)
            self.json_scope_stack.append(root_node)
            self.json_scope_stack.append(pair_node)

    def __add_object_node(self, object_node):
        parent = self.__parent()
        if parent:
            if parent.type == 'pair':
                parent.add_child(object_node)
                self.json_scope_stack.append(object_node)
            elif parent.type == 'array':
                parent.add_child(object_node)
                self.json_scope_stack.append(object_node)
        else:
            # no parent indicates the node is the first to be added.
            # We must create a root node of which all other nodes will be 
            # descendants.  The root node must be an array or object.
            # Since this node is an object it will be the root.
            self.json_scope_stack.append(object_node)

    def __add_array_node(self, array_node):
        parent = self.__parent()
        if parent:
            # create parent array
            # add node to array's children
            # add array to parent pair node's chilren
            # add array to scope stack
            # an array item does not get added to stack because
            # it cannot have any chilren
            if parent.type == 'pair':
                parent.add_child(array_node)
                self.json_scope_stack.append(array_node)
            elif parent.type == 'array':
                parent.add_child(array_node)
                self.json_scope_stack.append(array_node)
        else:
            # No parent indicates this node is the first to be added.
            # We must create a root node of which all other nodes will be 
            # descendants.  The root node must be an array or object.
            # Since this node is an array it will be the root
            self.json_scope_stack.append(array_node)

    def __add_text_node(self, text_node):
        parent = self.__parent()
        if parent:
            # LOGIC BUG may need to add text node to scope stack since 
            # text nodes can have children (literal or variable)
            if parent.type == 'pair':
                parent.add_child(text_node)
                self.json_scope_stack.append(text_node)
            elif parent.type == 'array':
                parent.add_child(text_node)
                self.json_scope_stack.append(text_node)
        else:
            # No parent indicates this node is the first to be added.
            # We must create a root node of which all other nodes will be 
            # descendants.  The root node must be an array or object.
            # Since this node is a text node the root node must be an array
            root_node = self.create('array')
            root_node.add_child(text_node)
            self.json_scope_stack.append(root_node)
            self.json_scope_stack.append(text_node)

class Node(object):
    def __init__(self, type = 'unknown'):
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class TextNode(Node):
    # children = ['literal', VariableNode('name'), 'literal', ...]
    def __init__(self, value, variable=False):
        super(TextNode, self).__init__('text')
        if variable:
            self.add_child(VariableNode(value))
        else:
            self.add_child(value)

    def render(self):
        # loop through children
            # link variables to value and concatenate children
        # the compiler will supply a link() function that returns an error
        # or the variables value
        # the link function looks up the variable name in the compilers symbol table
        pass

class VariableNode(Node):
    def __init__(self, name):
        self.name = name

class PairNode(Node):
# A pair's children can only contain a single node.  The child node's type 
# must be an object, an array, or a text node.  It CANNOT be
# another pair because a pair can only exist as the child of an object.
    def __init__(self, key):
        super(PairNode, self).__init__('pair')
        self.key = key

class ObjectNode(Node):
    def __init__(self):
        super(ObjectNode, self).__init__('object')

class ArrayNode(Node):
    def __init__(self):
        super(ArrayNode, self).__init__('array')
