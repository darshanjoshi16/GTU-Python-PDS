#Lab Assignment 4.6
#For the list of names: [Johnny, Russell, Scarlett, Russell, Johnny, Mark] and print the count of each element of the list.

#importing the counter function from collection module which counts elements
from collections import Counter

#creation of the list
lst = ['Johnny','Russell','Scarlett','Russell','Johnny','Mark']

#assigning the counter function
count = Counter()

# using for loop which will return the count of each element occuring
for i in lst:
    count[i] = count[i]+1

print(count)