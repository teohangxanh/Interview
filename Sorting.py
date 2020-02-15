'''
Author: Ted Dang
Description: 
    This programs is to sort a list of integers
    The only parameter is the list of integers to be sorted
'''

import math

#This function returns a list of digits of n from right to left
def getDigits(n):
    ans = []
    while n > 0:
        rem = n % 10
        ans.append(rem)
        n = int(n / 10)
    return ans

#Swap two numbers in a list using their indices
def swapPos(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
 
#Swap two numbers' remues
def swaprem(a, b):
    temp = a
    a = b
    b = temp
    
def shift_right(alist, left, right):
    if (left > right or len(alist) < left or len(alist) < right):
        return -1
    temp = alist[right]
    for i in range(right, left, -1):
        alist[i] = alist[i - 1]
    alist[left] = temp    
    
def a_bubble(alist):
    if len(alist) < 2:
        return alist
    for i in range(len(alist) - 1):
        #See if the list was already sorted
        swapped = False
        for j in range(len(alist) - 1 - i):
            if (alist[j] > alist[j + 1]):
                swapPos(alist, j, j + 1)
                swapped = True
        #As there is no swap, the list was already sorted      
        if (swapped == False):
            break
    return alist           
 
def d_bubble(alist):
    if len(alist) < 2:
        return alist
    for i in range(len(alist) - 1):
        #See if the list was already sorted
        swapped = False
        for j in range(len(alist) - 1 - i):
            if (alist[j] < alist[j + 1]):
                swapPos(alist, j, j + 1)
                swapped = True
        #As there is no swap, the list was already sorted      
        if (swapped == False):
            break
    return alist 

def a_selection(alist):
    if len(alist) < 2:
        return alist
    for i in range(len(alist)):
        min = alist[i]
        min_index = i
        for j in range(i, len(alist)):
            if alist[j] < min:
                min = alist[j]
                min_index = j
        if (alist[i] != min):
            swapPos(alist, min_index, i)
    return alist

def d_selection(alist):
    if len(alist) < 2:
        return alist
    for i in range(len(alist)):
        max = alist[i]
        max_index = i
        for j in range(i, len(alist)):
            if alist[j] > max:
                max = alist[j]
                max_index = j
        if (alist[i] != max):
            swapPos(alist, max_index, i)
    return alist
        
def a_insertion(alist):
    if len(alist) < 2:
        return alist
    #Consider from 1 to len
    for i in range(1, len(alist)):
        for j in range(i):
            if alist[i] < alist[j]:
                shift_right(alist, j, i)
                break
    return alist

def d_insertion(alist):
    if len(alist) < 2:
        return alist
    #Consider from 1 to len
    for i in range(1, len(alist)):
        for j in range(i):
            if alist[i] > alist[j]:
                shift_right(alist, j, i)
                break
    return alist

def a_shell(alist):
    if len(alist) < 2:
        return alist
    gap = int(len(alist) / 2)
    while (gap > 0):
        for i in range(len(alist) - gap):
            if alist[i] > alist[i + gap]:
                swapPos(alist, i, i + gap)
                #Check and back swap
                j = i
                while j - gap >= 0:
                    if alist[j] < alist[j - gap]:
                        swapPos(alist, j, j - gap)
                    j -= gap
        gap = int(gap / 2)
    return alist

def d_shell(alist):
    if len(alist) < 2:
        return alist
    gap = int(len(alist) / 2)
    while (gap > 0):
        for i in range(len(alist) - gap):
            if alist[i] < alist[i + gap]:
                swapPos(alist, i, i + gap)
                #Check and back swap
                j = i
                while j - gap >= 0:
                    if alist[j] > alist[j - gap]:
                        swapPos(alist, j, j - gap)
                    j -= gap
        gap = int(gap / 2)
    return alist

def a_radix(alist):
    digit = 0
    mx = 0
    
    #Find how many digits the max number has
    for i in range(len(alist)):
        mx = max(mx, alist[i])
        
    #If len(alist) is a power of 10 evenly
    if math.log(mx, 10) == math.floor(math.log(mx, 10)):
        digit = math.log(mx, 10)
    else:
        digit = math.floor(math.log(mx, 10)) + 1
    
    #i represents the number of digits of max
    newlist = alist.copy()
    sublist = [[], [], [], [], [], [], [], [], [], []]
    d = 1
    for i in range(digit + 1):
    #j stands for index of each number in the list
        d = d * 10
        for j in range(len(newlist)):
            while 
            rem = newlist[j] % d
            sublist[rem].append(newlist[j])
        print(sublist)
            
    return 0
    

            
        
    
    
    
    
        