#Lab Assignment 4.2
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

#creation of list
lst = [(1,2),(2,5),(3,6),(4,5),(5,9),(4,1),(6,2)]

#defined the last function which returns the last element of list
def last(n):
    return n[-1]

#defined the sorting function which sorts the list where the key is last which is defined in earlier function
def sort_list_last_key(tuples):
    return sorted(tuples,key=last)

print(sort_list_last_key(lst))