from abc import ABC,abstractmethod

class interface():

    @abstractmethod

    def enroll_from_course():
        pass

    def remove_from_course():
        pass

class student(interface):

    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def enroll_to_course(self,course) :
        self.temp="enrolled to"
        self.course=course

    def remove_from_course(self,course):
        self.temp="removed from"
        self.course=course
        

    def display(self) :
        print("\"{} {} is {} the course:{}\"".format(self.firstname,self.lastname,self.temp,self.course))

print("------------------------------------------------------------------------")
firstname = input(" Enter Your First Name:")
lastname=input(" Enter Your Last Name: ")
age=input(" Enter Your Age:")
print("------------------------------------------------------------------------")

s1=student(firstname,lastname,age)
choice=int(input(" Enter a 1 for enroll into course \n Enter 2 for removal from course\n Choose Your Option: "))


if choice==1:
    print("------------------------------------------------------------------------")
    course=input("Enter the name of the course you want to enroll: ")
    s1.enroll_to_course(course)

elif choice==2:
    print("------------------------------------------------------------------------")
    course=input("Enter the name of the course you want to remove from your learning list: ")
    s1.remove_from_course(course)

s1.display()
print("------------------------------------------------------------------------")