#Lab Assignment 1.3
#Write a Python program to convert days entered into months and days.

#taking total nummber of days as input from user
days_enter=int(input("Enter number of days you want to convert into month: ")) #for example: days_enter=45
month=int(days_enter/30) 
#Month is equal 45/30 which is 1
day=int(days_enter % 30) 
#day is equal to 45%30 which is 15
print("Number of days entered by user: ",days_enter)
print("----------------------------------------")
print("Number of Month: ",month)
print("Number of day: ",day)
