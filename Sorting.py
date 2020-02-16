'''
Author: Ted Dang
Description: 
    This programs is to sort a list of integers
    The only parameter is the list of integers to be sorted
'''

#Swap two numbers in a list using their indices
def swapPos(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
 
#Swap two numbers' values
def swapVal(a, b):
    temp = a
    a = b
    b = temp
    
def shift_right(a_list, left, right):
    if (left > right or len(a_list) < left or len(a_list) < right):
        return -1
    temp = a_list[right]
    for i in range(right, left, -1):
        a_list[i] = a_list[i - 1]
    a_list[left] = temp    
    
def a_bubble(a_list):
    if len(a_list) < 2:
        return a_list
    for i in range(len(a_list) - 1):
        #See if the list was already sorted
        swapped = False
        for j in range(len(a_list) - 1 - i):
            if (a_list[j] > a_list[j + 1]):
                swapPos(a_list, j, j + 1)
                swapped = True
        #As there is no swap, the list was already sorted      
        if (swapped == False):
            break
    return a_list           
 
def d_bubble(a_list):
    if len(a_list) < 2:
        return a_list
    for i in range(len(a_list) - 1):
        #See if the list was already sorted
        swapped = False
        for j in range(len(a_list) - 1 - i):
            if (a_list[j] < a_list[j + 1]):
                swapPos(a_list, j, j + 1)
                swapped = True
        #As there is no swap, the list was already sorted      
        if (swapped == False):
            break
    return a_list 

def a_selection(a_list):
    if len(a_list) < 2:
        return a_list
    for i in range(len(a_list)):
        min = a_list[i]
        min_index = i
        for j in range(i, len(a_list)):
            if a_list[j] < min:
                min = a_list[j]
                min_index = j
        if (a_list[i] != min):
            swapPos(a_list, min_index, i)
    return a_list

def d_selection(a_list):
    if len(a_list) < 2:
        return a_list
    for i in range(len(a_list)):
        max = a_list[i]
        max_index = i
        for j in range(i, len(a_list)):
            if a_list[j] > max:
                max = a_list[j]
                max_index = j
        if (a_list[i] != max):
            swapPos(a_list, max_index, i)
    return a_list
        
def a_insertion(a_list):
    if len(a_list) < 2:
        return a_list
    #Consider from 1 to len
    for i in range(1, len(a_list)):
        for j in range(i):
            if a_list[i] < a_list[j]:
                shift_right(a_list, j, i)
                break
    return a_list

def d_insertion(a_list):
    if len(a_list) < 2:
        return a_list
    #Consider from 1 to len
    for i in range(1, len(a_list)):
        for j in range(i):
            if a_list[i] > a_list[j]:
                shift_right(a_list, j, i)
                break
    return a_list

def a_shell(a_list):
    if len(a_list) < 2:
        return a_list
    gap = int(len(a_list) / 2)
    while (gap > 0):
        for i in range(len(a_list) - gap):
            if a_list[i] > a_list[i + gap]:
                swapPos(a_list, i, i + gap)
        
        gap = int(gap / 2)
                
    return a_list
        
        
        
        
        