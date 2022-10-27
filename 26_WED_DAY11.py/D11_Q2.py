from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
	# Write your code here.
    for i in range(n):
        maxCount=0
        for j in range(n):
            if arr[j]==arr[i]:
                maxCount+=1
        if maxCount>n/2:
            return arr[i]
        
    return -1  
print(findMajorityElement([4,2,3,6,5],2))  