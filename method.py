#! python3
# methods
# ----------------------------------------------------------------
# methods in class
# ----------------------------------------------------------------

# methods first parameter must be self or

class Foo:
    def method(self, x):
        return x * 2

f = Foo()
print(f.method(3))

