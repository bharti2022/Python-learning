class demo:
    name = 'sagar'
    def __init__(self, age=None):
        self.age = age
        
    @classmethod
    def getName(cls):
        return cls.name    
       
print(demo.getName())
obj=demo()
print(obj.getName())
demo.name='bharti'
print(demo().name)
print(demo.getName())

       
       
