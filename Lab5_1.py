#Lab Assignment 5.1
# Write a Python program to create a class Addressbook having name and contact number as the member attribute. 
# Define Accessor method to get the details of the member variables. 
# Define mutator method to set the value to the member attribute and a method to update the contact number of the user.

class AddressBook:
   
    def setvalues(self,name,contact_number):
        self.name=name
        self.contact_number=contact_number

    def getvalues(self):
        return self.name,self.contact_number


object1 = AddressBook()

name = input("Please Enter Your Name: ")
contact_number = int(input("Enter Your Contact Number: "))

object1.setvalues(name,contact_number)

name,contact_number = object1.getvalues()
    
print("==================================PHONE BOOK==================================================\n")
print("Name \t \t \t  Contact Number \n")
print(name+"\t \t \t  "+ str(contact_number))




