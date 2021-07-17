class point:
    
    def __init__(self,x=0,y=0):
        self.x = float(x)
        self.y = float(y)

    def translate(self,o,p,q):
        self.x = self.x + float(o)
        self.y = self.y + float(p)
        self.z = self.z + float(q)

    def __str__(self) :
        print("({:.2f},{:.2f},{:.2f})".format(self.x,self.y,self.z))

class point3D(point):
    
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z =  float(z)

    def translate(self,o,p,q):
        point.translate(self,o,p,q)

    def __str__(self) :
        print("({:.2f},{:.2f},{:.2f})".format(self.x,self.y,self.z))

print("------------------------------------------------------------------")
x=input("Enter a value of x:")
y=input("Enter a value of y:")
z=input("Enter a value of z:")

obj=point3D(x,y,z)

dx=input("Enter a value of dx:")
dy=input("Enter a value of dy:")
dz=input("Enter a value of dz:")

obj.translate(dx,dy,dz)
print("------------------------------------------------------------------")
obj.__str__()