class NodeTree(object):
    def __init__(self):
        self.root = None
        self.scope = []

    def add(self, node):
        node.on_add(self.__parent())

    def close_scope(self):
        current_node_in_scope = self.__parent()
        current_node_in_scope.on_exit_scope()

        next_node_in_scope = self.__parent()
        next_node_in_scope.on_child_exits_scope(current_node_in_scope)

    ################################
    #### Raw Scope Manipulators ####
    ################################

    def add_to_scope(self, node):
        self.scope.append(node)

    def remove_from_scope(self):
        self.scope.pop()


    def __parent(self):
        if len(self.scope) > 0:
            return self.scope[-1]
        else:
            # the scope is empty
            return None
