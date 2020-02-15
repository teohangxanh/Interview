'''
Author: Ted Dang
Description: 
    This programs is to answer interview questions
'''

import math

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

    