#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = []
    minus = []
    zero = []
    for i in arr:
        if i > 0:
            plus.append(i)
        elif i < 0:
            minus.append(i)
        else:
            zero.append(i)
    
    print("{:.6f}".format(len(plus)/len(arr)))
    print("{:.6f}".format(len(minus)/len(arr)))
    print("{:.6f}".format(len(zero)/len(arr)))
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
