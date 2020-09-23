#! python3

# ----------------------------------------------------------------
# Write a Python class to convert an integer to a roman numeral
# ----------------------------------------------------------------
 
# ----------------------------------------------------------------
# what are the roman numeral characters?
# 1 = I, 2 = II, 3 = III, 4 = IV, 
# 5 = V, 6 = VI, 7 = VII, 8 = VIII, 
# 9 = IX, 10 = X, 11 = XI, 12 = XII,
# 1000 = M, 500 = D, C = 100, L = 50,
# ----------------------------------------------------------------
'''
class RomanNumeral():
    def __init__(self, number):
        self.one_thousand = 'M'
        self.five_hundreds = 'D'
        self.one_hundred = 'C'
        self.fifty = 'L'
    
    def convert(self, number):
        if number >= 1000:
            number = number % 1000 + number % 100
        elif number < 1000 and number >= 500:
            number = number % 500 + number % 100
        elif number < 500 and number >= 100:
            number = number % 100 + number % 50
        elif number < 100 and number >= 50:
        else number < 50:
            number = number % 10 + number % 5

'''

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(2))
print(py_solution().int_to_Roman(4000))
print(py_solution().int_to_Roman(1999))
print(py_solution().int_to_Roman(8))


