from os import *
from sys import *
from collections import *
from math import *
def isVowel(a):

    return (a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u')
def reverseVowels(s):
    # Write your code here.
    vowels = []
    s = list(s)
    for i in range(len(s)):
        if (isVowel(s[i])):
            vowels.append(s[i])
    # Reversing the vowels
    vowels = vowels[::-1]
    j = 0
    for i in range(len(s)):
        if (isVowel(s[i])):
            s[i] = vowels[j]
            j += 1

    return ''.join(s)