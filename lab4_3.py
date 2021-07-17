#Lab Assignment 4.3
# Write a Python program to remove duplicates from a list.

# creation of list
lst = []

#taking the amount of elements of list from user
num = int(input("Enter the number of elements you want to enter: "))

#appending the elements into the list
for i in range(num):
    number = int(input("Enter the number: "))
    lst.append(number)

print("Before the operation")
print("\n-------------------------------------------------")
print(lst)
print("\n After the Operation")
print("\n-----------------------------------------------------")

#Set function removes the duplicates into list and returns the list without the redundancy
print(set(lst))