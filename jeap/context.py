class Context(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get(self, identifier, *args):
        scope = None
        try:
            scope = getattr(self, identifier)
            for accessor in args:
                if accessor.accessor_type == 'attribute':
                    try:
                        scope = getattr(scope, accessor.key)
                    except AttributeError:
                        raise
                elif accessor.accessor_type == 'member':
                    try:
                        scope = scope[accessor.key]
                    except KeyError:
                        raise
        except AttributeError:
            pass
        except KeyError:
            pass

        return scope
