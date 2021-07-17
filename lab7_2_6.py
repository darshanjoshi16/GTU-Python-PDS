import numpy as np
import time

def takeArray(a,n,m):
    
    print("\n Enter the data of matrix: ")
    print("\n =========================================================================")


    for i in range(n):
        for j in range(m):
            a.append(int(input("Enter the Number: ")))

def Multi(a,b,c,n1,m2,n2):
    
    sum = 0

    for i in range(n1):
        for j in range(m2):
            sum = 0

            for k in range(n2):
                sum += a[i][k] * b[k][j]

            c.append(sum)

a = []
b = []
c = []

print("\n =========================================================================")
n1,m1,n2,m2=[int(n) for n in input("Enter n1Xm1 for matrix a and n2Xm2 for matrix b := ").split()]

takeArray(a,n1,m1)
takeArray(b,n2,m2)

a=np.array(a)
a=a.reshape((n1,m1))

b=np.array(b)
b=b.reshape(m1,n1)

print("\n =========================================================================")
print("matrix a :=\n",a)

print("\n =========================================================================")
print("matrix b :=\n",b)

if m1==n2:
    start1=time.time()
    Multi(a,b,c,n1,m2,n2)
    end1=time.time()
    
    c=np.array(c)
    c=c.reshape(n1,m2)
    print("\n Multiplication using vectorization method:=\n",c)
    print("\n Time complexity := ",start1-end1)

else:
    print("Here, no. of columns in matrix1 is not equal to no. rows in of matrix 2")

if m1==n2:
    start2=time.time()
    c=np.dot(a,b)
    end2=time.time()
    print("\n Multiplication using dot method :=\n",c)
    print("\n Time complexity := ",start2-end2)

else:
    print("Here, no. of columns matrix1 is not equal to no. rows of matrix 2")