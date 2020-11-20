#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    current_pos = 0
    while current_pos + 2 <= len(c):
        if c[current_pos] == 1:
            result += 1
            current_pos += 1
        elif c[current_pos] == 0:
            result += 1
            current_pos += 2
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
