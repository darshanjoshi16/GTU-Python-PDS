#Lab Assignment 2.5
#Write a Python program to create a very simple pizza-ordering menu. 
# At this pizzeria, there’s only one kind of pizza you can order: cheese pizza withno toppings. 
# Your choices are what size of pizza, and how many of them. You’ll need to figure out the total price of the order.
#  A small pizza costs Rs. 200, a medium Rs. 350, and a large Rs. 500.

# Greeting Text Input
name=input("Please Enter your name: ")

print("Welcome to Wonders of Pizzeria")
print("\n ======================================================")
print("Myself Pepperoni, Your Own Pizza helper...")
print("There’s only one kind of pizza you can order: cheese pizza with no toppings.")
print("Let me help you order a pizza")
print("What size would you like? \n A)small(200/-) \n B)Medium(350/-) \n C)Large(500/-)")

# \u001b[1m is used for making characters bold 
size=input("Enter the option you want to choose: \u001b[1m")

if(size=='a'):
    total=200
    s="Small"

if(size=='b'):
    total=350
    s="Medium"

if(size=='c'):
    total=500
    s="Large"

print('\u001b[0m',end='')

print("OK, ",s," that is ",total,"Rs. each")

num=int(input('How many would you like:\u001b[1m'))

print('\u001b[0m',end="")
total=(total*num)
print("Mr."+name+" Your total is:",total)
print("Have a good day!!!!")