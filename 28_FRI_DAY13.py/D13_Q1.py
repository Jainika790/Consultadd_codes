#Find frequency of duplicate characters
#char is the no. of characters, s is string, n is length of string
#Task was to return all duplicated string with its frequency...

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def duplicate_char(s: str, n: int):
    # Write your code here.
    char = 255
    freq = [0] * char
    for i in range(len(s)):
        freq[ord(s[i])] += 1

    arr = []
    for i in range(char):
        if freq[i] > 1:
            arr.append((chr(i), freq[i]))
    return arr

