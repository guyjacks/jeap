from jeap.indent_parser import SpaceIndentFSM as fsm
def test_base():
    spaces_per_indent = 4
    sif = fsm.SpaceIndentFSM(spaces_per_indent)
    # an indent is 4 spaces
    space = ' '
    indent = 4 * space

    actual = sif.transition()
    expected = 'space_1'
    assert expected == actual

    actual = sif.transition()
    expected = 'space_2'
    assert expected == actual

    actual = sif.transition()
    expected = 'space_3'
    assert expected == actual

    actual = sif.transition()
    expected = 'indent_counted'
 
    actual = sif.transition()
    expected = 'space_1'
    assert expected == actual

    """
    # transition to the indent_counted state
    # space_2
    sif.transition()
    # space_3
    sif.transition()
    # indent_counted
    sif.transition()
    """
