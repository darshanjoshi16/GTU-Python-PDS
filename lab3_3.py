#Lab Assignment 3.3
#Write a Python function to calculate the factorial of a number (a non-negative integer).


#defined the factorial function using recursion method
def Fact_R(n):
    """ Suppose n is an int which is greater than 0 and gives n! """
    if(n == 1):
        return 1
    else:
        return n * Fact_R(n-1)

#defined the function using Iterative loop method
def Fact_I(m):
    fact=1
    for i in range(1,m+1) :
        fact*=i
    
    return fact

#Taking input from user
number = int(input("Enter the number for which you want: "))

print("Factorial of Recursive way: ",Fact_R(number))
print("Factorial of Iterative way: ",Fact_I(number))