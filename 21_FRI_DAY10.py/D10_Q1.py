#QUESTION TO CHECK FOR VALID PALINDROME
#ALSO CHECK IF WE GET A PALINDROME AFTER REMOVING ANY ONE STRING

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def isPalindrome(s: str, i: int, j:int) -> bool:
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True
#print(isPalindrome("AKDM",5,1))
        
    
def validPalindrome(n: int, s: str) -> bool:
    i=0
    j=n-1
    
    while i<j:
        if s[i]!=s[j]:
            return(isPalindrome(s,i+1,j) or isPalindrome(s,i,j-1))
        i=i+1
        j=j-1
    return True
#print(validPalindrome(1,"ALAMALA"))