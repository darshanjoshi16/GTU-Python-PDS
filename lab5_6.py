class Student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("\n Name: {:} \n Roll Number: {:} \n Marks: {:}".format(self.name,self.rollno,self.marks))

class grace():
    @staticmethod

    def editmarks(obj):
        obj.marks = int(obj.marks)+10

name = input("Enter the name of student: ")
rollno = input("Enter the roll number: ")
marks = input("Enter the Marks of student: ")

s = Student(name,rollno,marks)
grace.editmarks(s)

print("--------------------------------------------------------------------------------------------------")
s.display()
