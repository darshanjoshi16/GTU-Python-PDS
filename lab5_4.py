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


choice=0
while choice!=4 :
    print("\nEnter 1 for display name\nEnter 2 for display DOB\nEnter 3 for total number of employee\nEnter 4 for exit")
    
    choice=int(input("Please Enter Your Choice: "))
    if choice==1 :
        emp1.display_name()
        emp2.display_name()
        print("-----------------------------------------------------------------------------------------------")

    elif choice==2 :
        emp1.display_dob()
        emp2.display_dob()
        print("-----------------------------------------------------------------------------------------------")

    elif choice==3:
        emp1.display_emp_count()
        print("-----------------------------------------------------------------------------------------------")
        
    
    elif choice==4:
        exit()

