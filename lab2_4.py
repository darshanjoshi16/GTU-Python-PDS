#lab assignment 2.4
#Write PYTHON programs to get the following patterns:


# take number of lines as input from users for each pattern
line_1=int(input("Enter a number of line for pattern1:"))
line_2=int(input("Enter a number of line for pattern2:"))
k=1

# logic for the first numerical pattern
print("Pattern1:")
for i in range(line_1):
    for j in range(i+1):
        print(k,end="")
        k+=1
    print()

#logic for second symbolic special character pattern 
print("Pattern2:")
for i in range(line_2):
    for z in range(line_2-i-1):
        print(" ",end="")
    
    for j in range(i+1):
        if(i%2==0) :
            print("#",end="")
        else :
            print("!",end="")
    print()