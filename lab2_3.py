#Lab Assignment 2.3
#Write a Python program to Insert a string ’12.5#4.56#7.22’ and the output should be the sum of the numbers separated by #..

#Here take thev input from the user and use the split() function with seperator/delimiter as "#"
number=(float(n) for n in input("Enter the string as per example 12.3#45.6#78.9: ").split("#"))

# Logic for summation of splitted number
sum = 0
for i in number:
    sum = sum + i

print("The sum of digits seperated by # is: ",sum)