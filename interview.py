'''
Author: Ted Dang
Description: 
    This programs is to answer interview questions
'''

import math
from numpy import random

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
    return fact(n) // (fact(n - k)) * fact(k))

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
    
'''public int[] fix34(int[] nums) {
  int len = nums.length;
  List<Integer> l = new ArrayList<Integer>(); 
  for (int i = 0; i < len; i++){
    if (nums[i] == 4) {
      l.add(i);
    }
  }
  int count = 0;
  for (int i = 0; i < len; i++){
    // If needed to replace nums[i]
    if (i + 1 < len && nums[i] == 3){
      nums[l.get(count)] = nums[i+1];
      nums[i+1] = 4;
      count++;
    }

  }
  return nums;
}'''








