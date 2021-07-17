import numpy as np

print("=============================================================")
n1 = int(input("Enter the lower bound limit of array: "))
n2 = int(input("Enter the upper bound limit of array: "))

arr = np.arange(n1,n2,10)
print("\n=============================================================")
print("\n",arr)

print("\n=============================================================")
print("\n",arr.reshape(5,2))


