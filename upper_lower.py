#!/usr/bin/env python

text = input('please input sentence here:')
if text.islower() == True:
    New_text = text.upper()
else:
    New_text = text.lower()
new_word =''.join(New_text)
print(new_word)
