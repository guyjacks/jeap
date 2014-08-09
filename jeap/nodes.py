import operator

class Node(object):
# ATTENTION: compiler will create a tree and then set it as the value for 
# Node.tree.  This way, all intances have access to it
# ast = NodeTree()
# Node.tree = ast
    def __init__(self, tree = None):
        self.type = None
        self.children = []
        self.tree = tree

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

    def _get_effective_parent_type(self):
        # forking requires us to check the root type before adding 
        # nodes to the prong.  the prong's root type becomes the 
        # effective type for determining whether or not this node
        # should be added
        parent = self.tree.get_scoped_node()
        effective_parent_type = parent.type
        if effective_parent_type == 'prong':
            effective_parent_type = parent.root.type
        return effective_parent_type

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
            RootNode(self.tree).add()
            self.add()
        else:
            effective_parent_type = self._get_effective_parent_type()
            self.__add_to_tree(effective_parent_type)

    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type in ('pair', 'array', 'root'):
            parent = self.tree.get_scoped_node()
            parent.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise exception
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
            RootNode(self.tree).add()
            self.add()
        else: 
            effective_parent_type = self._get_effective_parent_type()
            self.__add_to_tree(effective_parent_type)

    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type in ('pair', 'array', 'root'):
            parent = self.tree.get_scoped_node()
            parent.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise exception
            pass

class PairNode(Node):
    def __init__(self, tree = None):
        """
            @key: must be a ValueNode
        """
        super(PairNode, self).__init__(tree)
        self.type = 'pair'
        self.key = None

    def add(self):
        parent_node = self.tree.get_scoped_node()
        if parent_node.type == 'value':
            # set key value
            self.key = parent_node
            # remove the parent value node from the scope
            self.tree.close_scoped_node() 

            # add pair to the tree
            parent_node = self.tree.get_scoped_node()
            if parent_node == None:
                ObjectNode(self.tree).add()
            effective_parent_type = self._get_effective_parent_type()
            self.__add_to_tree(effective_parent_type)
     
        else:
            # Raise exception
            pass
   
               
    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type != 'object':
            ObjectNode(self.tree).add()
        self.tree.get_scoped_node().add_child(self)
        self.tree.add_to_scope(self)

    def child_exits_scope(self, child_node):
        self.tree.close_parent_node()

class ValueNode(Node):
    """
        a value is one of the following; a pair key, a pair value, or an array item
    """
    def __init__(self, tree = None):
        super(ValueNode, self).__init__(tree)
        self.type = 'value'

    def add(self):
        parent_node = self.tree.get_scoped_node()

        if parent_node == None:
            RootNode(self.tree).add()
        effective_parent_type = self._get_effective_parent_type()
        self.__add_to_tree(effective_parent_type)
                
    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type in ('pair', 'array'):
            self.tree.get_scoped_node().add_child(self)
        self.tree.add_to_scope(self)

    def close(self):
        # if parent node is not already object, pair, or array then
        # create an array to store this value
        pass

class LiteralNode(Node):
    def __init__(self, value, value_type, tree = None):
        self.type = 'literal'
        self.value = value
        # string, bool, or number
        self.value_type = value_type
        super(LiteralNode, self).__init__(tree)
     
    def add(self):
        parent = self.tree.get_scoped_node()
        if parent == None:
            RootNode(self.tree).add()
            self.add()
        else:
            effective_parent_type = self._get_effective_parent_type()
            self.__add_to_tree(effective_parent_type)

    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type != 'value':
            ValueNode(self.tree).add()
        self.tree.get_scoped_node().add_child(self)

#### Flow Control Nodes ####
class LoopNode(object):
    def __init__(self, expression):
        pass

class ForkNode(Node):
    def __init__(self, tree = None):
        super(ForkNode, self).__init__(tree)
        self.type = 'fork'
        self.root = None

    def add(self):
        parent_node = self.tree.get_scoped_node()
        if parent_node == None:
            root_node = RootNode(self.tree)
            root_node.add()
            self.add()
        else:
            parent_node.add_child(self)
            self.tree.add_to_scope(self)
            self.root = parent_node

class ProngNode(Node):
    def __init__(self, tree = None):
        super(ProngNode, self).__init__(tree)
        self.type = 'prong'
        self.root = None
        self.expression = None

    def add(self):
        parent_node = self.tree.get_scoped_node()
        if parent_node.type == 'fork':
            self.root = parent_node.root
            parent_node.add_child(self)
            self.tree.add_to_scope(self)
        else:
            # raise error
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
        if parent_node == None:
            root_node = RootNode()
            root_node.add()

        if parent_node.type == 'fork':
            prong_node = ProngNode(self.tree)
            prong_node.add()
            prong_node.expression = self
            self.tree.add_to_scope(self)
        elif parent_node.type == 'loop':
            pass
        else:
            # {{ expr }}
            effective_parent_type = self._get_effective_parent_type()
            self.__add_to_tree(effective_parent_type)

    def __add_to_tree(self, effective_parent_type):
        if effective_parent_type == 'value':
            self.tree.get_scoped_node().add_child(self)
        elif effective_parent_type in ('root', 'array', 'object', 'pair'):
            value_node = ValueNode(self.tree)
            value_node.add()
            value_node.add_child(self)
        else:
            # raise exception
            pass
        self.tree.add_to_scope(self)

    def exit_scope(self):
# add set last_value to right of last operator (if applicable)
        pass

    def render(context):
#return self.expression_tree.root.evaluate()
        return self.expression.evaluate()

    def add_to_expression(self, node):
        self.expression.add_to_expression(node)

"""
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
"""


#### Store the priority (Order) of operations ####
or_op_priority = 1
and_op_priority = 2
# relational operator.are >,<,==, ...
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
        self.negate = False

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

class AndOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(AndOperatorNode, self).__init__(tree)
        self.priority = and_op_priority 

    def evaluate(self):
        return (self.left.evaluate() and self.right.evaluate())

class OrOperatorNode(OperatorNode):
    def __init__(self, tree = None):
        super(OrOperatorNode, self).__init__(tree)
        self.priority = or_op_priority 

    def evaluate(self):
        return (self.left.evaluate() or self.right.evaluate())

class NegateNode(Node):
    def __init__(self, tree = None):
        self.type = 'negate'

class RelationalOperatorNode(OperatorNode):
    def __init__(self, operation, tree = None):
        super(RelationalOperatorNode, self).__init__(tree)
        self.priority = relational_op_priority
        self.operation = operation

    def evaluate(self):
        result = None
        left = self.left.evaluate()
        right = self.right.evaluate()

        if self.operation == '<':
            result = operator.lt(left, right)
        elif self.operation == '<=':
            result = operator.le(left, right)
        elif self.operation == '==':
            result = operator.eq(left, right)
        elif self.operation == '!=':
            result = operator.ne(left, right)
        elif self.operation == '>':
            result = operator.gt(left, right)
        elif self.operation == '>=':
            result = operator.ge(left, right)
        elif self.operation == 'in':
            result = (left in right)

        if self.negate:
            result = not result
        return result
