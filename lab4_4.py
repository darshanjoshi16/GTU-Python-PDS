#Lab Assignment 4.4
#Write a Python program to check a list is empty or not.

#creation of list
lst = []

#taking the amount of elements in list from user
num = int(input("Enter the number of elements you want to enter: "))

#appending the elements into list
for i in range(num):
    number = int(input("Enter the number: "))
    lst.append(number)

#defining the isempty function,which returns the boolean values according to elements in your list
def isempty(lst):
    if(len(lst) == 0):
        print("The List is Empty")
    else:
        print("The List is not empty")

print(isempty(lst))