#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = 0
    if s == 'a':
        result = n
    else:
        result = s.count('a') * math.floor(n/len(s))
        for i in range(n % len(s)):
            if s[i] == 'a':
                result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
