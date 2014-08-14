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
    def __init__(self, node_tree = None, expression_tree = None):
        super(ExpressionNode, self).__init__(node_tree)
        self.type = 'expression'
        self.tree = node_tree
#self.expression = GroupNode(node_tree, expression_tree)
        self.expression = expression_tree

    def add(self):
        parent_node = self.tree.get_scoped_node()
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

    def add_child(self, node):
#self.expression.add_to_expression(node)
        self.expression.add(node)

    def exit_scope(self):
        self.expression.close()
        # IMPORTANT - I still need to remove this node from the node_tree

    def render(context):
        #return self.expression_tree.root.evaluate()
        return self.expression.evaluate()

class GroupNode(Node):
    def __init__(self, node_tree, expression_tree):
        self.type = 'group'
        self.tree = node_tree
        self.expression = expression_tree

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # raise error
            pass

class ExpressionLiteralNode(Node):
    
    def __init__(self, value, node_tree):
        self.type = 'expression_literal'
        self.tree = node_tree
        self.value = value
        self.negate = False

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # raise error
            pass

    def evaluate(self):
        if self.negate:
            return not self.value
        else:
            return self.value

    def __str__(self):
        if self.negate:
            return 'not ' + str(self.value)
        else: 
            return str(self.value)

class ExpressionVariableNode(Node):
    def __init__(self, identifier, node_tree):
        super(ExpressionVariableNode, self).__init__(node_tree)
        self.type = 'variable'
        self.identifier = identifier
        self.negate = False

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # raise error
            pass

    def evaluate(self, context):
        pass

    def __str__(self):
        value = self.identifier
        if self.negate:
            return 'not ' + self.identifier
        else:
            return self.identifier

class VariableAccessorNode(Node):
    def __init__(self, key, accessor_type, node_tree):
        super(VariableAccessorNode, self).__init__(node_tree)
        self.type = 'accessor'
        self.key = key
        self.accessor_type = accessor_type

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # error
            pass
         
class NegateNode(Node):
    def __init__(self, node_tree):
        self.type = 'negate'
        self.tree = node_tree

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # raise error
            pass

##############################
#### Begin Operator Nodes ####
##############################

#### Store the priority (Order) of operations ####
or_op_priority = 1
and_op_priority = 2
relational_op_priority = 3
add_or_subtract_op_priority = 4
multiply_or_divide_op_priority = 5
exponent_op_priority = 6

class OperatorNode(Node):
    def __init__(self, operation, node_tree):
        self.type = 'operator'
        self.operation = operation
        self.tree = node_tree
        self.left = None
        self.right = None

    def add(self):
        parent = self.tree.get_scoped_node()
        if parent.type == 'expression':
            parent.add_child(self)
        else:
            # raise error
            pass

    def evaluate(self):
        result = None
        left = self.left.evaluate()
        right = self.right.evaluate()

        if self.operation == '+':
            result = operator.add(left, right)
        elif self.operation == '-':
            result = operator.sub(left, right)
        elif self.operation == '*':
            result = operator.mul(left, right)
        elif self.operation == '/':
            result = operator.div(left, right)
        elif self.operation == '^':
            result = operator.pow(left, right)
        elif self.operation == 'and':
            result = left and right
        elif self.operation == 'or':
            result = left or right
        elif self.operation == '<':
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
        return result

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        space = ' '
        return str(self.left) + space + self.operation + space + str(self.right)

class AddOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(AddOperatorNode, self).__init__('+', node_tree)
        self.priority = add_or_subtract_op_priority 

class SubtractOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(SubtractOperatorNode, self).__init__('-', node_tree)
        self.priority = add_or_subtract_op_priority

class MultiplyOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(MultiplyOperatorNode, self).__init__('*', node_tree)
        self.priority = multiply_or_divide_op_priority

class DivideOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(DivideOperatorNode, self).__init__('/', node_tree)
        self.priority = multiply_or_divide_op_priority

class ExponentOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(ExponentOperatorNode, self).__init__('^', node_tree)
        self.priority = exponent_op_priority 

class AndOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(AndOperatorNode, self).__init__('and', node_tree)
        self.priority = and_op_priority 

class OrOperatorNode(OperatorNode):
    def __init__(self, node_tree):
        super(OrOperatorNode, self).__init__('or', node_tree)
        self.priority = or_op_priority 

class RelationalOperatorNode(OperatorNode):
    def __init__(self, operation, node_tree):
        super(RelationalOperatorNode, self).__init__(operation, node_tree)
        self.priority = relational_op_priority
