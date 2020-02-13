# -*- coding: utf-8 -*-
"""
Author: Ted Dang
Description: 
    This programs is to handle primes
'''
"""

#Check if a number is prime
def isPrime(n):
    flag = True
    if type(n) == int:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    else:
        return -1
    return flag

#Find all primes in a range
def findPrime(n):
    arr = []
    for i in range(2, n + 1):
        if isPrime(i):
            arr.append(i)
    return arr