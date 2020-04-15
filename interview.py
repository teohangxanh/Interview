'''
Author: Ted Dang
Description: 
    This programs is to answer interview questions
'''

import math
from numpy import random
import pandas as pd

# This calculate factorial of n
def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

# This returns permutation of n choose k in an equal probability
def permutation(n, k):
    return int(fact(n) / fact(n - k))

# This returns combination of n choose k in an equal probability
def combination(n, k):
    return fact(n) // (fact(n - k) * fact(k))

def isPalindrome(n):
    my_list = []
    n = math.floor(n)
    while n > 0:
        rem = n % 10
        my_list.append(rem)
        n = int(n / 10)
    for i in range(len(my_list)):
        if my_list[i] is not my_list[len(my_list) - i - 1]:
            return False
    return True
        
def findMin(alist):
    mn = alist[0]
    for i in range(len(alist)):
        if mn > alist[i]:
            mn = alist[i]
    return mn
        
def findMax(alist):
    mx = alist[0]
    for i in range(len(alist)):
        if mx < alist[i]:
            mx = alist[i]
    return mx

'''Given 2 sorted arrays of integers, code to find a number from each array 
such that their sum is closest to some integer K'''
def question3(alist, blist, k):
    my_list = [[] for _ in range(len(alist))]
    for i in range(len(alist)):
        numa = alist[i]
        for j in range(len(blist)):
            numb = blist[j]
            my_list[i].append(abs(numa + numb - k))
    mn = my_list[0][0]
    for lst in my_list:
        for number in lst:
            if mn > number:
                mn = number
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] == mn:
                a = alist[i]
                b = blist[j]
    return a, b

def displayFib(n):
    ans = [0] * n
    for i in range(n):
        if i < 2:
            ans[i] = 1
        elif i>= 2:
            ans[i] = ans[i - 1] + ans[i - 2]
    return ans



# This returns a list of n uniformly random numbers from a to b
def uniform(n, a, b):
    result = []
    for i in range(n):
        number = random.uniform(a, b)
        result.append(number)
    return result
    
''' Given a non-empty array, return true if there is a place to split the 
array so that the sum of the numbers on one side is equal to the sum of the 
numbers on the other side '''
def canBalance(alist):
    leng = len(alist)
    i = 0
    j = leng - 1
    l = 0
    r = 0
    while i <= j:
        if l < r:
            l += alist[i]
            i += 1
        elif l > r:
            r += alist[j]
            j -= 1
        else:
            if i == j:
                return alist[i] == 0
            else:
                l += alist[i]
                i += 1
                r += alist[j]
                j -= 1
    return l == r
    
''' 
Return an array that contains exactly the same numbers as the given array, 
but rearranged so that every 3 is immediately followed by a 4. Do not move 
the 3's, but every other number may move. The array contains the same number 
of 3's and 4's, every 3 has a number after it that is not a 3, and a 3 appears 
in the array before any 4. '''
def fix34(alist):
    l = []
    # l stores indices of four's in alist
    for i in range(len(alist)):
        if alist[i] == 4:
            l.append(i)
    count = 0
    for i in range(len(alist)):
        if i + 1 < len(alist) and alist[i] == 3:
            alist[l[count]] = alist[i+1]
            alist[i+1] = 4
            count += 1
    return alist
    
'''Check if subsets of a set l can sum up to a number s'''
def check_subset_sum(s, l):
    l.insert(0, 0)
    r = [[0 for i in range(s+1)] for j in range(len(l))]
    for i in range(len(l)):
        for j in range(s+1):
            if j == 0:
                r[i][j] = 1
            else:
                if j < l[i]:
                    r[i][j] = r[i-1][j]
                else:
                    r[i][j] = r[i-1][j] or r[i-1][j - l[i]]
    return(bool(r[-1][-1]))
    index = [i for i in l]
    columns = [i for i in range(s+1)]
    r = pd.DataFrame(r, index, columns)
    print(r)

'''Return a list of items which sums up to the max value with the weight <= a given weight'''
def knapsack(w, wl, vl):
    r = [[0 for x in range(w+1)] for y in range(len(vl))]
    for i in range(len(vl)):
        for j in range(w+1):
            up = r[i-1][j]
            val = vl[i]
            left = r[i-1][j - wl[i]]
            if j == 0:
                r[i][j] = 0
            elif i == 0:
                # If weight of item < max weight
                if wl[i] <= j:
                    r[i][j] = val
            else:
                # If weight of item < max weight
                if wl[i] > j:
                    r[i][j] = up
                else:
                    r[i][j] = max(val + left, up)
                
    trace_back = []
    i = len(r) - 1
    j = len(r[0]) - 1
    while i != 0 and j != 0:
        up = r[i-1][j]
        val = vl[i]
        left = r[i-1][j - wl[i]]
        cur = r[i][j]
        if cur == up:
            i -= 1
        else:
            trace_back.append([wl[i], vl[i]]) 
            j -= wl[i]
            i -= 1
    # Print (weight, value)
    print(trace_back)
    
    # index = [[x for x in vl],[x for x in wl]]
    # columns = [x for x in range(w+1)]
    # r = pd.DataFrame(r, index, columns)
    # print(r)
    # for i in range(w+1):
    #     print(i, end='\t')
    # print()
    
    
'''Find the longest common subsequence of two strings'''
def longest_common_subsubsequence(s1, s2):
    r = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    for i in range(len(r)):
        for j in range(len(r[0])):
            left = r[i][j-1]
            up = r[i-1][j]
            diag = r[i-1][j-1]
            if i == 0:
                r[i][j] = 0
            else:
                if j > 0:
                    if s1[i-1] == s2[j-1]:
                        r[i][j] = 1 + diag
                    else:
                        r[i][j] = max(left, up)
                
    trace_back = []
    i = len(r) - 1
    j = len(r[0]) - 1
    while i > 0 and j > 0:
        cur = r[i][j]
        left = r[i][j-1]
        up = r[i-1][j]
        diag = r[i-1][j-1]
        if cur == left:
            j -= 1
        elif cur == up:
            i -= 1
        else:
            trace_back.insert(0, s2[j-1])
            i -= 1
            j -= 1
            
    print(trace_back)   
    index = [x for x in s1]
    index.insert(0, 0)
    columns = [x for x in s2]
    columns.insert(0, 0)
    r = pd.DataFrame(r, index, columns)
    print(r)
    
    
s1 = 'acbcf'          
s2 = 'abcdaf'
(longest_common_subsubsequence(s1, s2))














