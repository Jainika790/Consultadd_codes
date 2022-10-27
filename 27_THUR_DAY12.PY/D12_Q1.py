from os import *
from sys import *
from collections import *
from math import *

def ninjaCandidate(arr):
    # Write your code here.
    n=len(arr)
    arr.sort()
    
    takelastthree=arr[n-3] * arr[n-2] * arr[n-1]
    takefirsttwo=arr[0] * arr[1] * arr[n-1]
    
    return max(takelastthree,takefirsttwo)
    
    
print(ninjaCandidate([2,4,5,1,3]))