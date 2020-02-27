
# import sorting
import math
import random
import sorting
import interview

#Prompt the user to input the name of the file
#fileName = input("Enter the file containing numbers to be sorted\n")

#Open the file
#my_file = open(fileName, 'r')
# my_file = open('1.txt', 'r')

#Create a list to store the numbers in the file
# my_list = []
a_list = []
for i in range(100):
    num = random.randint(0, 1000)
    a_list.append(num)

a_list.clear()
a_list = [2, 3, 4, 1, 2]
#Read the file and copy the numbers to my list
# with open('1.txt', 'r') as f:
#     for line in f:
#         int_list = [int(i) for i in line.split(' ')]
#         my_list = int_list.copy()

print(interview.findIndex(a_list))
        
#Close the file
# my_file.close()
