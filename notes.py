# 1  modify tokenizer
## A  add states for emitting literals and variables before discovering a pair separator ... "blah {{ x }} = value {{ y }}\n"
### i    emit token('literal', 'blah ')
### ii   emit token('variable', 'x')
### iii  emit token('pair_sep', ' ') # emits the space between variable and '='
### iv   emit token('literal', ' value ')
### v    emit token('newline', "")

# 2  modify compiler
## A  add transitions to handle new tokens emitted by the tokenizer
## B  modify __end_indent
### i  use the syntax_tree classe's json_scope_stack instead of compiler's

# 3  unit tests
## A  SyntaxTree
### i   test_add_node
### ii  test_create_node
## B  Compiler
### i  test_compile
## C  Tokenizer
### i  test_interpret with new states for variables

person = 
    first=guy # must have 1 indent
    last=jacks # must have 0 or 1 indents
               # if 0 then its a dedent closing the object
               # if 1 its a pair in the same parent (no indent)
               # if > 1 then its an error: only array items and pair values can be nested
person =
    first=troy
    last=jacks # dedent on the next line closes this nested object and the pair
person = 
    first=guy
    last=jacks

