#Lab Assignment 3.7
# Write a Python function that that prints out the first n rows of Pascal's triangle.

# defining the function for printing Pascal's Triangle
def printpascal(n):
    k=2*n-2
    for line in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k-=1
        for i in range(0,line+1):
            print(num_print(line,i)," ",end="")
        print("")

#defining function for calculation of which number needed to  print in pascal's triangle
def num_print(n, k):
    num=1
    if(k>n-k):
        #if the row and column values are same, then it returns 1 to the above method.
        k=n-k
    for i in range(0,k):
        num=num*(n - i)
        num=num//(i + 1)
    return num

#Taking the input from the user
N = int(input("Enter the number of row you want to print for pascal triangle: "))

print(printpascal(N))


