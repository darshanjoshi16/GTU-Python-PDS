#Lab Assignment 3.2
# Write a python function to multiply all the function in a list 

#importing the reduce function from functools module 
from functools import reduce 

#creation of list
lst = []

#Taking input from users and appending those numbers into the list.
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

#Using Lambda function x,y got converted into x*y in lst and initial value is 1
#The reduce() function will apply the function to the elements of the iterable using the rolling result cumulatively before it arrives at a final output value.
mul = reduce(lambda x, y: x*y,lst,1)
print(lst)
print(mul)
