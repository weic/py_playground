#! python3
'''
a = 0
while a < 5:
    s = input('input your name:')
    if s == 'haha':
        print('your name is {0}'.format(s))
        break
    else:
        a += 1
        print('a=', a)
print('the end a', a)

'''
#continue and its usage
b = 11
while b > 0:
    b -= 1
    if b % 2  == 0:
        #continue
        print(b)
    else:
        print(b)
