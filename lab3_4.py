#Lab Assignment 3.4
#Write a Python function that takes a number as a parameter and check the number is prime or not.

# defining prime function with using for loop and if statements
def prime(num):
    for i in range(2,num):
        if((num % i) == 0):
            return 0
        else:
            return 1

#taking input from users
n = int(input("Enter the number you want to check: "))
result = prime(n)

print(n," is a prime number" )if(result == 1) else print(n, " is not a prime number")
