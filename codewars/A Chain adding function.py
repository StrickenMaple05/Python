class add(int):
    def __call__(self, x):
        return add(self + x)


print(add(3)(2)(4))
