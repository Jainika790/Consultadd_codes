#CHECK SUBSET
#checks if array 2 is subset of array1 such that all elements of array2 is present in array1.

from os import *
from sys import *
from collections import *
from math import *

def checkSubset(arr1, arr2, n, m):
    # Write your code here.    
    if m > n:
        return False
    for i in range(m):
        j = 0
        while(j < n):
            if arr2[i] == arr1[j]:
                arr1[j] = -1
                break
            j += 1
        if j == n:
            return False
    return True
print(checkSubset([1,2,4,6],[1,2,4],4,3))
