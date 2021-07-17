#Lab Assignment 2.2
#Write a Python program to print the series of prime numbers until the number entered by the user.

#take the input from user
number=int(input("Enter the number: "))
print("-----------------------------------------------------------")

print("The Prime Numbers come before "+str(number)+" are: ")

# here j is running from numbers which are less than the number entered by user
for j in range(2,number):
    k=0
# here i is running from 2 to j to see j is divisible by i or not divisible.
    for i in range (2,j):
        if(j % i == 0):
            k=1
# k is determining the status of reminder if it is 1, it is not prime.        
    if(k != 1):
        print(j,end=" ")

        
print("\n ----------------------------------------------------------")
