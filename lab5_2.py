s = []

class create_account_num:
    
    def __iter__(self):
        self.account_number = 1
        return self

    def __next__(self):
        x = self.account_number
        self.account_number += 1
        s.append(x)
        return x

class BankAccount:
   
    def setaccount(self,name):
        self.name = name
        self.account_number = next(myiter)
        self.balance = 0

    def getaccount(self):
        return self,self.name,self.account_number,self.balance

    def deposit(self):
        amount = float(input("Enter the Deposit Amount: "))
        self.balance += amount

        print(amount," is deposited in your account")
        print("Balance in your account is ",self.balance)

    def withdraw(self):
        amount = float(input("Enter the Amount You want to withdraw: "))

        if (self.balance > amount):
            self.balance -= amount
            print("Withdrawn Amount: ",amount)
            print("The Balance is: ",self.balance)
        else:
            print("Invalid Transaction.Amount should be less than Balance in your account")

    def valid(self,account_number):
        for i in s:
            if (i == account_number):
                return 1
            else:
                return 0

    def display(self):
        print("Account Holder Name : ",self.name)
        print("Account Number: ",self.account_number)
        print("Balance in Account: ",self.balance)


class_it_number = create_account_num()
myiter = iter(class_it_number)

name = input("Enter the Name: ")

object1 = BankAccount()
object1.setaccount(name)

choice=0

while choice!=5 :
    print("\n Enter 1 for display details \n Enter 2 for deposit in account\n Enter 3 for withdraw proceedure\n Enter 4 for check valid account number\n Enter 5 for exit: ")

    choice=int(input())
    if choice==1 :
        object1.display()

    elif choice==2 :
        object1.deposit()

    elif choice==3:
        object1.withdraw()

    elif choice==4:
        acount_number=int(input("Enter a acount number which you want to check:"))
        print("Valid account number") if object1.valid(acount_number) else print("Not valid account number")

    elif choice==5:
        exit()


