#Lab Assignment 1.7
#Write a Python program to evaluate the sum of integers between a and b entered by the user that is divisible by 3.

#taking the lower bounds and upper bounds for given operation.
number1=int(input("Enter the first number for range: "))
number2=int(input("Enter the second number for range: "))

sum=0

# running for loop from upper to lower bound
for i in range(number1,number2):
    if((i%3)==0):
        sum=sum+i

# example:
# num1 is 5 and num2 is 10.
# in this range only 6 and 9 are integers which are divisible by 3
# so the answer would be summation of those integers. which is 15

print("-------------------")
print("The sum of integer which are divisible by 3 between ",number1," and ",number2," is ",sum)
