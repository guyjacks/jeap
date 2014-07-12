import ast

SPACES_PER_INDENT = 4
SPACE = ' '
INDENT = SPACE * SPACES_PER_INDENT
TAB = '\t'
PAIR_SEPARATOR = '='
NEWLINE = '\n'
ARRAY_OPEN = '['
ARRAY_CLOSE = ']'
OBJECT_OPEN = '{'
OBJECT_CLOSE = '}'
VAR_START = '{{'
VAR_FILTER_SEPARATOR = '|'
VAR_FILTER_ARGUMENT_SEPARATOR = ','
VAR_END = '}}'
BLOCK_OPEN = '{%'
BLOCK_FOR_CMD = 'for'
BLOCK_IF_CMD = 'if'
BLOCK_ELSE_CMD = 'else'
BLOCK_ELIF_CMD = 'elif'
BLOCK_END_CMD = 'end'
BLOCK_CLOSE = '%}'
ESCAPE = "\\"
QUOTE = '"'

class Node(object):
    pass

class Root(Node):
    pass

# parse yields fragments
# [indents][pair_key=]value\n

def compile(template):
    root = Root()
    parent_indent_count = 0
    scope = [root]
    indents, fragments = parse_line(template)
    for fragment in fragments:
        parent_node = scope[-1]
        if indents < parent_indent_count:
            parent_node.exit_scope()
            scope_stack.pop()
    node = self.create_node(fragment)
    if node:
        parent_node.children.append(node)
        if indents > parent_indent_count:
            scope_stack.append(node)
            node.enter_scope()
