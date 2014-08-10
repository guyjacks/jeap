class NodeTree(object):
    def __init__(self):
        self.root = None
        self.scope = []

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
        self.last_value = None
        self.negate_next = False
        # group is True when there is an open expression group in scope
        self.group = False
        self.closed = False

    def add(self, node):

        if self.negate_next:
            node.negate = True
            self.negate_next = False

        if self.group:
            self.last_value.add_to_expression(node)
        else:
            if node.type == 'group':
                self.add_group_node(node)
            elif node.type == 'operator':
                self.add_operator_node(node)
            elif node.type == 'literal':
                self.add_literal_node(node)
            elif node.type == 'negate':
                self.add_negate_node(node)
            else:
                # raise error
                pass

    def add_group_node(self, node):
        self.last_value = node
        self.group = True

    def add_operator_node(self, node):
        last_operator = self.last_operator
        last_value = self.last_value
        if last_operator == None:
            # this is the first operator node of the expression
            node.left = last_value
            self.root = node
        elif node <= last_operator:
            last_operator.right = last_value
            node.left = last_operator
            self.root = node
        elif node > last_operator:
            node.left = last_value
            last_operator.right = node
            self.root = last_operator
        else:
            # raise exception
            pass
        self.last_operator = node

    def add_literal_node(self, node):
        self.last_value = node

    def add_negate_node(self, node):
        self.negate_next = True

    def close(self):
        if self.group:
            self.last_value.close()
            if self.last_value.tree.closed:
                self.group = False
        else:
            self.last_operator.right = self.last_value
            self.closed = True
