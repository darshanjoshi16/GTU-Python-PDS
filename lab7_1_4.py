import numpy as np

print("=======================================================================")
n3=int(input("\n Enter total number of elements you want to enter: "))
c = []

for i in range(1,n3+1):
    s = input("Enter the String: ")
    c.append(s)

arr = np.array(c)
print("=======================================================================")
print("\n",arr)