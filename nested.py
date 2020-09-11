#! python3
'''
lst = [1, 2, 3]
lst.append(4)
print(lst)

def foo(f):
    f()
    return f()
print(foo)



def z():
    print('this is a test')
def x(z):
    z()
print(x(z))


def opt_seq(func, seq):
    r = [func(i) for i in seq]
    return r

print(opt_seq(abs, range(-5, 5)))
print(opt_seq(str, [1, 2, 3]))
print(opt_seq(ord, 'python'))
'''

# nonlocal 
'''
G = mg, g = 9.8
'''

def w(m, g):
    return m * g

def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg

w = weight(10)
G = w(100)
G2 = w(50)
print(G)

w = weight(9.78046)
G3 = w(100)
print(G3)

