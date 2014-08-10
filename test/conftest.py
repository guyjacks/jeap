import pytest
@pytest.fixture()

def node_tree():
    import jeap.tree as tree
    import jeap.nodes as nodes
    return tree.NodeTree(nodes.RootNode())
