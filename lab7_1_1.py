
import numpy as np


print("=======================================================================")
n1=int(input("Enter total number of elements you want to enter: "))
a=[]

for i in range(0,n1):
    a.append(int(input("Enter the element: ")))

arr1=np.array(a)


print("=======================================================================")
n2=int(input("\n Enter total number of elements you want to enter: "))
b = []


for i in range(0,n2):
    b.append(float(input("Enter the element: ")))

arr2 = np.array(b)


print("=======================================================================")
n3=int(input("\n Enter total number of elements you want to enter: "))
c = []


for i in range(0,n3):
    c.append(input("Enter the element: "))

arr3 = np.array(c)


print("\n=====================================================================")
print("\n Integer Array : ",arr1)
print("\n Float Array : ",arr2)
print("\n Character Array : ",arr3)



