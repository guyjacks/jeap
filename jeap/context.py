class Context(object):
    def __init__(self, **kwargs):
        self.symbols = {}
        for k, v in **kwargs:
            self.set(k, v)

    def set(self, name, value):
        self.symbols['name'] = value

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            # raise error
            pass
