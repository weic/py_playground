#! python3
# different class
# ----------------------------------------------------------------
# class property 
# ----------------------------------------------------------------

# static
class foo:
    lang = 'python'

print(foo.lang)

f = foo()
print(f.lang)

foo.group = 'this'
print(f.group)

f.name = 'name is wrong'
print(f.name)

foo.group = 'that'
print(f.group)

# Dynamic property
class bar:
    def __init__(self, name):
        self.name = name
b = bar('haha')
c = bar('heihei')
print(b.name)
print(c.name)
print(bar)
print(b.__dict__)

# Class initialize
class Bar:
    def __init__(self):
        print(self)
x = Bar()
print(x)

