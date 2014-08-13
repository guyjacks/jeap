class NodeTree(object):
    def __init__(self, root = None):
        self.root = None
        self.scope = []
        if root:
            root.tree = self
            root.add()

    def add(self, node):
        node.add()

    def close_scoped_node(self):
        current_node_in_scope = self.get_scoped_node()
        current_node_in_scope.exit_scope()

        next_node_in_scope = self.get_scoped_node()
        next_node_in_scope.child_exits_scope(current_node_in_scope)

    ################################
    #### Raw Scope Manipulators ####
    ################################

    def add_to_scope(self, node):
        self.scope.append(node)

    def remove_scoped_node(self):
        return self.scope.pop()

    # Replaces __parent
    def get_scoped_node(self, position = 1):
        if position > 0:
            position = -position

        if len(self.scope) > 0:
            return self.scope[position]
        else:
            # the scope is empty
            return None

class ExpressionTree(object):
    def __init__(self):
        self.root = None
        self.last_operator = None
        self.operator_scope = []
        self.last_value = None
        self.negate_next = False
        # group is True when there is an open expression group in scope
#self.group = False
#self.closed = False
        self.type = 'expression_tree'
        # is_group is used by __str__.
        # if is_group is true then __str__ will enclose value in '(' & ')'
        self.is_group = False
        self.negate = False
        self.open = True

    def add(self, node):

#if self.group:
        if self.last_value != None and self.last_value.type == 'expression_tree' and self.last_value.open:
#self.last_value.add_to_expression(node)
            self.last_value.add(node)
        else:
            if node.type == 'group':
                self.add_group_node(node)
            elif node.type == 'operator':
                self.add_operator_node(node)
            elif node.type == 'variable':
                self.add_variable_node(node)
            elif node.type == 'accessor':
                self.add_variable_accessor_node(node)
            elif node.type == 'expression_literal':
                self.add_literal_node(node)
            elif node.type == 'negate':
                self.add_negate_node(node)
            else:
                # raise error
                pass

    def add_group_node(self, node):
#       self.last_value = node
        self.last_value = node.expression
        self.last_value.negate = self.negate_next
        self.last_value.is_group = True
        self.negate_next = False
#        self.group = True

    def add_operator_node(self, node):
        node.negate = self.negate_next
        self.negate_next = False

        last_operator = self.last_operator
        last_value = self.last_value
        if last_operator == None:
            # this is the first operator node of the expression
            node.left = last_value
            self.root = node
        elif node <= last_operator:
            last_operator.right = last_value
#node.left = last_operator
#self.root = node
            use_next = False
            next_found = False
            for n in reversed(self.operator_scope):
                if use_next:
                    n.right = node
                    next_found = True
                    break

                if node >= n:
                    node.left = n
                    use_next = True
            if next_found == False:
                node.left = self.operator_scope[0]
                self.root = node
        elif node > last_operator:
            node.left = last_value
            last_operator.right = node
#self.root = last_operator
        else:
            # raise exception
            pass
        self.last_operator = node
        self.operator_scope.append(node)

    def add_variable_node(self, node):
        print('var', node.type, node.identifier)
        node.negate = self.negate_next
        self.negate_next = False
        self.last_value = node

    def add_variable_accessor_node(self, node):
        self.last_value.add_child(node)

    def add_literal_node(self, node):
        node.negate = self.negate_next
        self.negate_next = False
        self.last_value = node

    def add_negate_node(self, node):
        self.negate_next = True

    def close(self):
        if self.last_value:
            if self.last_value.type == 'expression_tree' and self.last_value.open:
                self.last_value.close()
            else:
                if self.last_operator:
                    self.last_operator.right = self.last_value
                else:
                    # in this case the expression contains only a group
                    # i.e. (2 + 2)
                    # or its a single value
                    # i.e. True
                    self.root = self.last_value
                self.open = False
        else:
            # error - tree must have a value to call close()
            pass

    """
    def close(self):
        if self.group:
            self.last_value.close()
            if self.last_value.tree.closed:
                self.group = False
        else:
            self.last_operator.right = self.last_value
            self.closed = True
    """
    def evaluate(self):
        value = self.root.evaluate()
        if self.negate:
            return not value
        else:
            return value

    def __str__(self):
        value = str(self.root)
        if self.is_group:
            value = '(' + value + ')'

        if self.negate:
            value = 'not ' + value

        return value
