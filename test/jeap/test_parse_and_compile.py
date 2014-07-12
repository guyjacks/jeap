import jeap.jeap as jeap
space = ' '
indent = 4 * space
def test_object_base():
    input = 'key1=\n'
    input += indent + 'key2=value1\n'
    input += indent + 'key3=value2\n'

    jeap = jeap()
    jeap.parse_and_compile(input)
    root = jeap.ast.root

    assert root.type == 'object'
    assert len(root.children) == 1
    child = root.children[0]
    assert child.type == 'pair'
    assert child.key == 'key1'
    assert len(child.children) == 1
