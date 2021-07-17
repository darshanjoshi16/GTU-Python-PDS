#Lab Assignment 1.5
#Write a Python program to evaluate the power function using while loop.

# taking value of base and exponent from user
base = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))

#checking if the value of exponent is not negative
if (exponent>0):
    answer=base

elif (exponent==0):
    answer=1
    
#calculating the answer
while(exponent > 1) :
    answer=answer * base
    exponent=exponent-1

print("Answer is:",answer)