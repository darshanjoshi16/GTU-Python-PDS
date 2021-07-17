#Lab Assignment 4.5
#Write a Python function that takes two lists and returns True if they have at least one common member.


#creation and appending the elements into lst by user
lst = []

num = int(input("Enter the number of elements you want to enter in first list: "))

for i in range(num):
    number = int(input("Enter the number: "))
    lst.append(number)


#creation and appending the elements into lst1 by user
lst2 = []

num = int(input("Enter the number of elements you want to enter in second list: "))

for i in range(num):
    number = int(input("Enter the number: "))
    lst2.append(number)


# defining the common element function which returns the true or false according to your common elements in both list.
def common_ele(lst,lst1):
    for i in lst:
        for i in lst1:
            return True
    return False

print(common_ele(lst,lst2))