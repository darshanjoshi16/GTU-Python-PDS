#Lab Assignment 1.2
# Write a Python program to find the greatest of 3 numbers.

#taking input from users
x=input("Enter the first number:")
y=input("Enter the second number:")
z=input("Enter the third number:") 

#using if and elif for finding largest number among entered number
if (x>y) and (x>z):
    print("The greatest number: "+x)

elif (y>x) and (y>z):
    print(" The greatest number: "+y)

else:
    print(" The greatest number: "+z)


