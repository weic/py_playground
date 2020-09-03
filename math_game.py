#! python3

import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, Evelyn, this program requires Python 3.x," 
    "please ask Daddy to help you\n")
    sys.exit(1)

'''
This is a python mini game for kid to do:
Addition 
Subtraction 

In the future, it will include:
Multiplication
Division
'''
import math
import random
import time


a = random.randint(1, 20)
b = random.randint(1, 20)
print('Hi Evelyn, please wait for the computer to give you the question in 2 seconds')
time.sleep(1)
for i in range(2, 0, -1):
    time.sleep(1)
    print(i)
print('Go!!!')
time.sleep(1)
print('What is the value of:')
print(a, ' + ', b)
m = input('Answer:')
n = a + b
if int(m) == n:
    print('Good job Evelyn! The answer', n, 'is correct!')
else:
    print('Oh no, the answer is incorrect!')
    time.sleep(1)
    print('Give you another 2 seconds to try again.')
    for i in range(2, 0, -1):
        time.sleep(1)
        print(i)
    x = input('Answer again:')

    if int(x) == n:
        print('Good job Evelyn! The answer', n, 'is correct!')
    else:
        print('Still incorrect! Only 2 chances, you should try a different question')


    




