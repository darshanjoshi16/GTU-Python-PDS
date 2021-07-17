#lab Assignment 2.6
#Write a program called time.py that prompts the user to enter the current time in HH:MM format, and then prints a message that states the time in a sentence.

# take the time input from user and use split() function with ":" as a delimiter or separator
a,b=[int(n) for n in input("Enter a time (HH:MM) example 9:30 :").split(":")]

# checking the validness of entered time by user
if (a > 12 or b > 60):
    print ("invalid Entry")
    exit()

if (b==60):
    a+=1
    b-=60

print("It is now",b," minutes after",a," o'clock.")