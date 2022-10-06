class demo:
    age=20
    def __init__(self, id=None):
        self.id=id
        
    def method1(self): #methods in python
        return(self.age*0.3)    

obj1 = demo(10)
obj1.name= "sagar"
print(obj1.name)
print(obj1.id)
print(obj1.age)
print(obj1.method1())
        
        