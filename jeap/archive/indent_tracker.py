class IndentTracker:
    def __init__(self):
        space = ' '
        tab = '\t'
        self.parent_indent_count
        self.current_indent_count
        
        # can be configured to use tabs
        # will try to detect indent char automatically
        self.indent_char = space

        # can be configured
        # autodetect is possible
        self.spaces_per_indent = 4

    def calculate_indent_count(self, input):
        pass

    def validate(self):
        # check to see that the current indent level is no more than one greater than the parent
        pass


