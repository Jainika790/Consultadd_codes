from collections import *
from math import *
from os import *
from sys import *


def countOnBits(num):
    # Write your code here.
    ans=0
    while(num>0):
        ans=ans+(num%2)
        num //=2
    return ans
    pass
print(countOnBits(10))