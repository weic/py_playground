#!/usr/bin/env python

origin_word = str(input('please input word here:'))
shift_letter = int(input('please input how many letter you\'d like to shift:'))

lst = list(origin_word)
crypText = []
new_word = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z']

for letter in lst:
    if letter in alphabet:
        index = alphabet.index(letter)
        crypting = (index + shift_letter) % 26
        crypText.append(crypting)
        newLetter = alphabet[crypting]
        new_word.append(newLetter)

new_word = ''.join(new_word)
print(new_word)




