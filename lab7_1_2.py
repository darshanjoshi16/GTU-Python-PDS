#Practical Lab Assignment 7.1.2
# Create an array of 1 to 20 in reverse order using arange function.

#importing numpy library

import numpy as np 

n = int(input("Enter the size of Array:  "))
a = []

for i in range(0,n):
    a.append(i)

arr = np.array(a)

#in arange function (n-1) defines starting value, -1 is stopping value which is not included and last one is for difference in elements
print(arr[np.arange(n-1,-1,-1)])