class MetaThing(type):
    """MetaThing metaclass"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Thing(metaclass=MetaThing):
    """Thing class"""

    def __init__(self, name=None):
        self.name = name


jane = Thing('Jane')
print(jane.name)
jane.is_a.woman = True
print(jane.is_a.woman)

