class JsonPrinter:
    def __init__(self, indent):
        self.indent = indent

    def print_object_open(self, indent_count):
        indents = indent_count * self.indent
        return indents + '{'

    def output_object_close(self, indent_count):
        pass

    def output_array_open(self, indent_count):
        pass

    def output_array_close(self, indent_count):
        pass

    def output_string(self, indent_count, input):
        pass

    def output_number(self, indent_count, input):
        pass

    def output_pair_separator(self):
        pass

    def print_indents(self, indent_count):
        return indent_count * self.indent


