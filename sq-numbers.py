class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def sqSum(self):
        return (self.x**2+self.y**2+self.z**2)
    
obj1 = Point(1, 2, 3)
print(obj1.sqSum())            