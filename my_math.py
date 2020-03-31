
import numpy as np

'''
Author: Ted Dang
Usage: This programs is to handle primes
'''
#Check if a number is prime
def isPrime(n):
    if type(n) == int:
        if n == 2:
            return True
        elif n < 2 or n % 2 == 0:
            return False
        else:
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    return False
    return True

'''
Author: Ted Dang
Usage: This programs is to find all primes in a range
'''
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
    #In primes, value == 1 means the value of the index is the prime
                primes[i * j] = 0
                
    #Copy primes into a new list
    for i in range(len(primes)):
        if primes[i] == 1:
            answer.append(i)
    return answer

'''
Author: Ted Dang
Usage: This programs is to find all factors of a number
'''
def findFactors(n):
    answer = [1]
    increment = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.insert(increment, int(i))
            increment += 1
            # If n = i^2, (n / i) counts
            if int(n ** 0.5) != i:
                #This is to keep the factors sorted in ascending order
                answer.insert(increment, int(n / i))
    #Prepend n to the list as it's also a factor of itself
    answer.insert(len(answer), n)
    return answer

'''
Author: Ted Dang
Usage: This programs is to find all prime factors of a number
'''
def findPFactors(n):
    #Keys <- factors, values <- powers
    ans = {}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count = 0
            #Count = power of the factor
            while n % i == 0:
                n /= i
                count += 1
            ans[i] = count
    ans[int(n)] = 1
    return ans
            
'''
Author: Ted Dang
Usage: This programs is to find Greatest Common Divisor
'''
def gcd(a, b):
    if type(a) == int and type(b) == int:
        return a if b == 0 else gcd(b, a % b)
    else:
        return -1
'''
Author: Ted Dang
Usage: This programs is to find the Fn number of a fibonaci starting
from a and b. For example, the series = a, b, a+b, b + a+b, etc.
'''
def findFib(a, b, n):
    phi = (1 + 5 ** 0.5) / 2
    return 0 if n < 0 else round((phi ** n) / (5 ** 0.5))