#Lab assignment 3.6
#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

#creation of list
lst = []
lst1 = []

#defining the square function for the elements of list
def square(lst):
    for i in range(1,31):
        temp = i*i
        if(temp < 31):
           
           # appending the value of i into lst
            lst.append(i)

            # appending the value of i squared into lst1
            lst1.append(temp)

# calling the square function
square(lst)
print("Input List: ",lst)
print("\n --------------------------------")
print("\n",lst1)