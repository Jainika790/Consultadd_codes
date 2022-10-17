from collections import *
from math import *
from os import *
from sys import *


def isCyclicRotation(p,q):
    n = len(p)
    for j in range(n):
        isRotationPossible = 1
        for i in range(n):
            if (p[(i + j) % n] != q[i]):
                isRotationPossible = 0
                break
        if (isRotationPossible):
            return 1
    return 0 