#Lab Assignment 1.6
#Write a Python program to evaluate the factorial function using while loop.

#taking the number for which user want to find factorial
number=int(input("Enter the value for which you want to get factorial value:"))

#determining the value of fact and running while loop for calculation
fact=1
i=1
while (i<=number):
    fact=fact*i
    i=i+1

# example: number is 3. fact is 1. the while loop will run from, i=1 to i=3 in which fact will be multiplying with i and i will be incrementing 1
print("factorial of ",number,"is",fact)
