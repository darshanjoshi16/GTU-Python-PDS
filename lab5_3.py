import math
class point:
    
    def __init__(self,x=0,y=0):
        self.x = float(x)
        self.y = float(y)

    def distance_origin(self):
        return ((self.x ** 2)+(self.y ** 2))**0.5

    def distance_other(self,o,p):
        dx = (self.x - o)
        dy = (self.y - p)

        return ((dx ** 2)+(dy ** 2))**0.5

    def translate(self,o,p):
        self.x = self.x + float(o)
        self.y = self.y + float(p)

    def __str__(self):
        print("({:.2f},{:.2f})".format(self.x,self.y))


x=input("Enter a value of x: ")
y=input("Enter a value of y: ")
object1=point(x,y)
print("\n-------------------------------------------------------------------------\n")
print("Distance from origin",object1.distance_origin())
print("Distance from other point (2.0,4.3) ",object1.distance_other(2.0,4.3))
print("\n-------------------------------------------------------------------------\n")
dx=input("Enter a value of dx: ")
dy=input("Enter a value of dy: ")
print("\n-------------------------------------------------------------------------\n")
object1.translate(dx,dy)
object1.__str__()