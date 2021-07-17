#Lab Assignment 1.4
#Write a Python program to find the roots of a Quadratic equation.

# importing math library from installed libraries
import math

#taking value of a,b,c in quadratic equation
a=int(input("Enter the value for A:"))
b=int(input("Enter the value for B:"))
c=int(input("Enter the value for C:"))

# using formula of d
d=((b*b)-(4*a*c))

#using if-elif for checking of roots from value of d 
if (d>0):
    print("First Root:",(((-b) +math.sqrt(d))/(2*a)))
    print("Second Root:",((-b -math.sqrt(d))/(2*a)))

elif (d<0):
    print("Real Root does not exist")

else:
    print("Root :",((-b)/(2*a)))