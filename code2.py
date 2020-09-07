class SigmaAlgebra(set):
    def __init__(self, sample_space):
        super().__init__((frozenset(sample_space), frozenset()))

    def __or__(self, other):
        print('or')
        super().__or__(other)

    def add(self, other):
        print('add')
        super().add(other)

    @classmethod
    def _wrap_methods(cls, names):
        def wrap_method_closure(name):
            def inner(self, *args):
                result = getattr(super(cls, self), name)(*args)
                # if isinstance(result, set) and not hasattr(result, 'foo'):
                #     result = cls(result, foo=self.foo)
                return result
            inner.fn_name = name
            setattr(cls, name, inner)
        for name in names:
            wrap_method_closure(name)


