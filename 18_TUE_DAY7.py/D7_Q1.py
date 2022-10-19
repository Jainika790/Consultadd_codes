from collections import *
from math import *
from os import *
from sys import *
from typing import *


def parityMove(a: List[int], n: int)-> List[int]:

    # Write your Code here
    for i in range(n):
        a[i] = a[i]%2
    a.sort()
    return a
    pass