class MyParentClass():
    def __init__(self, x, y):
        print("parentclass super",x,y)

class SubClass(MyParentClass):
    def __init__(self, x, y):
        print("child class method",x,y)
        super().__init__(x, y)
        
obj = SubClass(2,3)
# obj.__init__(2,3)        