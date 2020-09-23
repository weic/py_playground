#! python3
# Polymorphic
def add(x, y):
    return x + y

print(add(3, 4))
print(add('this', 'that'))

# Packaging, privatizing
# double underline __

class Foo:
    __name = 'abc'
    book = 'python'

print(Foo.book)


