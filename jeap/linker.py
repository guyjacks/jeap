class Linker(object):
    def __init__(self, symbols):
        self.symbols = symbols

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            # raise error
            pass
