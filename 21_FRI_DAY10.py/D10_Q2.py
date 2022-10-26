from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Write your code here
    R = -1
    M = -1
    
    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                R = arr[i]
                break

    currentSum = 0
    for i in range(n):
        currentSum += arr[i]
    actualSum = n * (n + 1) // 2
    M = actualSum - (currentSum - R)
    ans = M, R
    return ans
#print(missingAndRepeating(5,6))