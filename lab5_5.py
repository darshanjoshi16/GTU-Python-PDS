class EMP:
    
    count = 0
    
    def __init__(self,name,dd,mm,yy):
        EMP.count += 1

        self.name  = name
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def display_name(self):
        print("Employee Name: "+self.name)
    
    def display_emp_count(self):
        print("Total Number of Employees: ",EMP.count)

    def display_dob(self):
        print("Date of Birth:{:}/{:}/{:}".format(self.dd,self.mm,self.yy))

print("-----------------------------------------------------------------------------------------")

name = input("Enter Your Name: ")
dd,mm,yy=input("Enter a dd/mm/yy in this format:").split("/")
emp1=EMP(name,dd,mm,yy)

print("-----------------------------------------------------------------------------------------")

name = input("Enter Your Name: ")
dd,mm,yy=input("Enter a dd/mm/yy in this format:").split("/")
emp2=EMP(name,dd,mm,yy)

print("-----------------------------------------------------------------------------------------")


emp1.age = 22
print("\n Employee1 Salary")

try:
    getattr(emp1,"salary")

except AttributeError:
    print("Does not exist salary in emp1") 

else:
    print("Does exist salary in emp 1")

del emp1.age

print("\n Employee 1 data: ")
print("\n------------------------------------------------------------------------------------------")

emp1.display_name()
emp1.display_dob()

try:
    getattr(emp1,"age")

except AttributeError:
    print("Does not exist age in emp1")

else :
    print("Exists age in emp1") 

print("\n Employee 2 Data:")
print("\n------------------------------------------------------------------------------------------")

emp2.display_name()
emp2.display_dob()

try:
    getattr(emp2,"age")

except AttributeError:
    print("Does not exist age in emp2")

else :
    print("Exists age in emp2")

