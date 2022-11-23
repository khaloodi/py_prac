#!/usr/bin/env python

"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""

def rot13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    
    ctr = 0
    nw_string = ""

    for idx, i in enumerate(message):
        pos = abc.index(i)
        print(pos)
        if (i in abc) and (idx < 13):
            nw_string += abc[pos + 13]
        elif (i in abc) and (idx >= 13):
            nw_string += abc[pos - 13]    
    
    return nw_string

print(rot13('test'))