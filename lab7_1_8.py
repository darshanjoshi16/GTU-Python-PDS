import numpy as np

print("==================================================")
n1 = int(input("\n Enter the number of Rows:"))
n2 = int(input("\n Enter the number of columns: "))

arr = np.random.normal(15,10,(n2,n1))

print("\n==================================================")
print("\n",arr)