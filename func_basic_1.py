#! python3
# 函数 def 
#   def function_name(x, y, z):
#       do something return object

def addition(x, y):
    r = x + y
    return r

print(addition(1,2))
print(addition('aaa', 'bbb'))
print(addition([1, 2, 3], [4, 5, 6]))

def convert(a):
    lst = [i.upper() if i == i.lower() else i.lower() for i in a]
    return ''.join(lst)
 
a = 'Hello'
c = convert(a)
print(c)

print(addition(y=100, x=500))



