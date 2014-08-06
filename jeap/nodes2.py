import operator
class NodeFactory(object):
    def __init__(self):
        self.tree = None

    """
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
    """

class Node(object):
# ATTENTION: compiler will create a tree and then set it as the value for 
# Node.tree.  This way, all intances have access to it
# ast = NodeTree()
# Node.tree = ast
    def __init__(self, tree = None):
        self.type = None
        self.children = []
        self.tree = tree
    """
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
    """

    def enter_scope(self, current_parent):
        pass

    def add(self):
        # add the node to the node tree
        pass

    def exit_scope(self):
        self.tree.remove_scoped_node()


    def child_exits_scope(self, child_node):
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

    def add(self):
        self.tree.root = self
        self.tree.add_to_scope(self)

class ObjectNode(Node):
    def __init__(self, tree = None):
        super(ObjectNode, self).__init__(tree)
        self.type = 'object'

    def add(self):
        parent_node = self.tree.get_scoped_node()
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

    def add(self):
        parent_node = self.tree.get_scoped_node()
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

    def add(self):
# a pair must always be the child of an object
        parent_node = self.tree.get_scoped_node()
        if (parent_node is None) or (parent_node.type != 'object'):
            new_object_node = ObjectNode(self.tree)
#new_object_node.add_child(self)
            self.tree.add(new_object_node)
            self.tree.add(self)
        else:
            parent_node.add_child(self)
            self.tree.add_to_scope(self)

    def child_exits_scope(self, child_node):
# A pair's children can only contain a single node.  The child node's type 
# must be an object, an array, or a value node.  It CANNOT be
# another pair because a pair can only exist as the child of an object.
        self.tree.close_parent_node()

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

    def add(self):
        parent_node = self.tree.get_scoped_node()
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

    def add(self):
        parent_node = self.tree.get_scoped_node()
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

    def add(self):
        parent_node = self.tree.get_scoped_node()
        if parent_node.type == 'value':
            parent_node.add_child(self)
        elif parent_node.type == None:
            # this should create an array -- maybe
            pass
        else:
            # raise error
            pass

    def render(self):
        return self.value
    
#### Flow Control Nodes ####
class LoopNode(object):
    def __init__(self, expression):
        pass

class IfNode(object):
    def __init__(self, expression):
        pass

class ExpressionNode(Node):
    def __init__(self, tree = None, expression_tree = None):
        self.type = 'expression'
        super(ExpressionNode, self).__init__(tree)
        self.tree = tree
        #self.expression_tree = exp_tree
        self.expression = GroupNode(expression_tree)

    def add(self):
        parent_node = self.tree.get_scoped_node()
        if parent_node.type == 'if':
            pass
        elif parent_node.type == 'for':
            pass
        else:
            # {{ expr }}
            pass

    def exit_scope(self):
# add set last_value to right of last operator (if applicable)
        pass

    def render(context):
#return self.expression_tree.root.evaluate()
        return self.expression.evaluate()

    def add_to_expression(self, node):
        self.expression.add_to_expression(node)

#### Store the priority (Order) of operations ####
or_op_priority = 1
and_op_priority = 2
# relational operators are >,<,==, ...
relational_op_priority = 3
add_or_subtract_op_priority = 4
multiply_or_divide_op_priority = 5
exponent_op_priority = 6

class ExpressionLiteralNode(Node):
    def __init__(self, value, tree=None):
        self.type = 'literal'
        self.tree = tree
        self.value = value
        self.negate = False

    def add(self):
        pass

    def evaluate(self):
        if self.negate:
            return not self.value
        else:
            return self.value

class OperatorNode(Node):
    def __init__(self, tree):
        self.type = 'operator'
        self.tree = tree
        self.left = None
        self.right = None

    def add(self):
        # add this node to the node tree
        # sees parent is expression and calls parent's add_to_expression
        pass

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

class GroupNode(Node):
    def __init__(self, tree):
        self.tree = tree
        self.type = 'group'
        self.negate = False

    def add(self, node):
        pass

    def add_to_expression(self, node):
        self.tree.add(node)

    def close(self):
        self.tree.close()

    def evaluate(self):
        if self.negate:
            return not self.tree.root.evaluate()
        else:
            return self.tree.root.evaluate()

class AddOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(AddOperatorNode, self).__init__(tree)
        self.priority = add_or_subtract_op_priority 

    def evaluate(self):
        return operator.add(self.left.evaluate(), self.right.evaluate())

class SubtractOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(SubtractOperatorNode, self).__init__(tree)
        self.priority = add_or_subtract_op_priority

    def evaluate(self):
        return operator.sub(self.left.evaluate(), self.right.evaluate())

class MultiplyOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(MultiplyOperatorNode, self).__init__(tree)
        self.priority = multiply_or_divide_op_priority

    def evaluate(self):
        return operator.mul(self.left.evaluate(), self.right.evaluate())

class DivideOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(DivideOperatorNode, self).__init__(tree)
        self.priority = multiply_or_divide_op_priority

    def evaluate(self):
        return operator.div(self.left.evaluate(), self.right.evaluate())

class ExponentOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(ExponentOperatorNode, self).__init__(tree)
        self.priority = exponent_op_priority 

    def evaluate(self):
        return operator.pow(self.left.evaluate(), self.right.evaluate())

class RelationalOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(RelationalOperatorNode, self).__init__(tree)
        self.priority = relational_op_priority
