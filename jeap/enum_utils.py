class BiDirectionalEnum(object):
    def __init__(self):
        self.enum = {}
        self.reverse = []
        self.incrementor = 0

    def add(self, item):
        self.enum[item] = self.incrementor
        self.reverse.append(item)
        self.incrementor += 1
# IDEA: modify to allow enum.name.reverse or enum.name.name sugar
# store (name, enum_int) tuples in self.enum instead
# return self.enum[name][1] for enum.name to get the enumerated int

    def __getattr__(self, item):
        if item in self.__dict__['enum']:
            return self.__dict__['enum'][item]
        elif item in self.__dict__:
            # client is trying to access an object attribute
            return self.__dict__[item]
        else:
            raise AttributeError

    def get_reverse(self, item):
        if isinstance(item, int):
            # Make sure the item is in the list
            if item < len(self.__dict__['reverse']):
                return self.__dict__['reverse'][item]
            else:
                raise AttributeError
        else:
            raise AttributeError

    def __contains__(self, item):
        return item in self.enum
        
    def __hash__(self):
        #will need to implement if I want to use token as dict key
        pass
 
class Events(BiDirectionalEnum):
    def __init__(self):
        BiDirectionalEnum.__init__(self)
        self.add('text')
        self.add('digit')
        self.add('pair_separator')
        self.add('newline')
        self.add('tab')
        self.add('space')
        self.add('escape_char')
        self.add('control_char')
        self.add('quote')
        self.add('minus_sign')
        self.add('plus_sign')
        self.add('period')
        self.add('open_bracket')
        self.add('close_bracket')
        self.add('open_curly_brace')
        self.add('close_curly_brace')
        self.add('pound')

class Tokens(BiDirectionalEnum):
    def __init__(self):
        BiDirectionalEnum.__init__(self)
        self.add('indent')
        self.add('pair_key')
        self.add('literal')
        self.add('newline')
        self.add('comment')
        self.add('variable')
        self.add('loop')
        self.add('if')
        self.add('elif')
        self.add('else')
        self.add('end')
        self.add('end_of_input')
