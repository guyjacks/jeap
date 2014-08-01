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
