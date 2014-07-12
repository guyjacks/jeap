import unicodedata

class Interpreter:
    def __init__(self, char_type):
        # enum of char types
        self.char_type = char_type

        self.open_bracket = '['
        self.close_bracket = ']'
        self.open_curly_brace = '{'
        self.close_curly_brace = '}'
        self.percentage = '%'
        self.minus_sign = '-'
        self.plus_sign = '+'
        self.space = ' ' # should be space or tab depending on config
        self.tab = '\t'
        self.pair_separator = '=' # could make this value configurable
        self.escape = '\\'
        self.quote = '"'
        self.newline = '\n'
        self.control_chars = set(['"', '\\', '/', 'b', 'f', 'n', 'r', 't'])
        self.pound = '#'
        #control char u is special ... \u00f3 
        self.unicode_control_char = 'u'
        # NOTE can hex digits be capital letters as well?
        self.digits = '0123456789'
        self.hexadecimal_digits = 'abcdef' + self.digits

        # self.lower_alpha = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        # self.upper_alpha = set(['A'])
        # self.valid_symbols = set(['!', '@'])
        #self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def interpret(self, char):
        if char.isdigit():
            return self.char_type.digit
        if char == self.newline:
            return self.char_type.newline
        if char == self.space:
            return self.char_type.space
        if char == self.pair_separator:
            return self.char_type.pair_separator
        if char == self.open_bracket:
            return self.char_type.open_bracket
        if char == self.close_bracket:
            return self.char_type.close_bracket
        if char == self.open_curly_brace:
            return self.char_type.open_curly_brace
        if char == self.close_curly_brace:
            return self.char_type.close_curly_brace
        if char == self.quote:
            return self.char_type.quote
        if char == self.pound:
            return self.char_type.pound
        # unicode must be last since it will match any of the above
        if self.is_unicode(char):
            return self.char_type.text

    def is_unicode(self, char):
        # http://docs.python.org/2/library/unicodedata.html
        is_unicode = True
        try:
            unicodedata.name(unicode(char))
        except ValueError:
            is_unicode = False

        return is_unicode
