#Lab Assignment 2.1
#Write a Python program to print the list of odd numbers until the number entered by the user.

#take input from users
number=int(input("Enter the number:"))

print("----------------------------------------")
print("The ODD numbers before "+str(number)+" are:" )

# for loop for determining whether the current number is divisible by 2 or not divisible.
for i in range(number):
    if(i % 2 != 0):
        print(i,end=" ")

print("\n----------------------------------------")