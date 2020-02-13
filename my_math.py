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
    primes = []
    answer = []
    for i in range(int(n) + 1):
        primes.append(1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == 1:
            for j in range(2, int(n / i) + 1):
                primes[i * j] = 0
    for i in range(len(primes)):
        if primes[i] == 1:
            answer.append(i)
    return answer

#Find all factors of a number
def findFactors(n):
    answer = [1]
    right = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.append(int(i))
            if int(n ** 0.5) != i:
                right.append(int(n / i))
    for i in range(len(right) - 1, 0, -1):
        answer.append(right[i])
    answer.insert(len(answer), n)
    return answer
            
    
    
    