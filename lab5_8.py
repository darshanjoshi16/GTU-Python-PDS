from abc import ABC, abstractmethod


class shape(ABC):
    
    @abstractmethod
    
    def area(self):
        pass

class square(shape):

    def __init__(self,side):
        self.side = float(side)

    def area(self):
        return (self.side**2)

class rectangle(shape):
    
    def __init__(self,length,breadth):
        self.length = float(length)
        self.breadth = float(breadth)

    def area(self):
        return (self.length * self.breadth)

print("-----------------------------------------------------------------------")
print("\n Rectangle")
print("\n-----------------------------------------------------------------------")
l = float(input("Enter the value of length: "))
b = float(input("Enter the value of breadth: "))
rec1 = rectangle(l,b)
print(rec1.area())

print("\n-----------------------------------------------------------------------")
print("\n Square")
print("\n -----------------------------------------------------------------------")
s = float(input("Enter the value of Side length: "))

sq1 = square(s)
print(sq1.area())
