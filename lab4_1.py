#lab Assignment 4.1
# Write a Python program to change the position of every nth value with the (n+1)th in a list.

#creation of list
lst = []

#defined the function for changing the position
def change_pos(lst):
    " This function change the element at particular index with its successor indexed element in pair"
    length = len(lst)
    
    #Swapping operation for changing the elements
    for i in range(0,length,2):
     lst[i],lst[i+1] = lst[i+1],lst[i]

    return lst


# taking the input from user
num = int(input("Enter the number of element you want to add in list: "))

# appending the elements into list
for i in range(num):
    number = int(input("Enter the input: "))
    lst.append(number)

# calling the function we defined earlier
change_pos(lst)

print(lst)