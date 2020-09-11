#! python3

#Decorator

def p_deco(func):
    def wrapper(name):
        return '{0}'.format(func(name))
    return wrapper

@p_deco
def book(name):
    return 'the name of my book is {0}'.format(name)

py_book = book('python text book')
print(py_book)

