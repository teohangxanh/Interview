
# import sorting
import math
import interview

#Prompt the user to input the name of the file
#fileName = input("Enter the file containing numbers to be sorted\n")

#Open the file
#my_file = open(fileName, 'r')
my_file = open('1.txt', 'r')

#Create a list to store the numbers in the file
my_list = []

#Read the file and copy the numbers to my list
with open('1.txt', 'r') as f:
    for line in f:
        int_list = [int(i) for i in line.split(',')]
        my_list = int_list
        
alist = [-5, -2, 0, 3, 6, 5, 7, 8, 9]
blist = [-25, -22, -20, -11, 0]
print(interview.question3(alist, blist, 15))
        
#Close the file
my_file.close()
