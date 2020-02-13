# -*- coding: utf-8 -*-
"""
Author: Ted Dang
Description: 
    This programs is to handle primes
'''
"""

import math

#Check if a number is prime
def isPrime(a):
    if type(a) == int:
        if a < 2:
            return False
        flag = True
        for i in (2, math.sqrt(a)):
            if a % i == 0:
                flag = False
    else:
        return -1
    return flag
