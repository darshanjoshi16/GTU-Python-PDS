import numpy as np

print("==========================================")
a = float(input("\nEnter the starting element: "))
b = float(input("\nEnter the ending element: "))

arr = np.logspace(a,b,num=10,base=10,dtype=int)

print("==========================================")
print("\n",arr)