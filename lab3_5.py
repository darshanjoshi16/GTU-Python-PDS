#Lab Assignment 3.5
#Write a Python program to print the even numbers from a given list.

#creation of list
lst = []

#Taking input from users and appending those numbers into the list.
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

#printing the list before filtering the even numbers
print("Before the Operation")
print("\n ---------------------------------------------")
print(lst)
print("\n")

#defining the even numbers detection function
def even_num(b):
    return (b % 2 == 0)

# list function stored the filtered result of even_num from lst
result = list(filter(even_num,lst))

#printing the list after filtering the even numbers
print("After the Operation")
print("-------------------------------------------------")
print(result)