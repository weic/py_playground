#! python3
# generate int from 0-100, 
# input a int and guess
# compare the 2 numbers

import math
import random

a = random.randint(0, 100)

while True:
    b = int(input('please type your guess here:'))
    print(b)

    if b < 0 or b >= 100:
        print('The number is between 0 and 100')
        
    else:
        if a == b:
            print('Nice guess! Game over')
            break
        elif a > b:
            print('Guess bigger!')
        else:
            print('Not a good guess! Try again please.')
            
