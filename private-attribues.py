class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property
    def method1(self):
        print(self.__salary)        
    def __privatemethod(self):
        print("this is private method")

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
Steve.method1()
# Steve.__privatemethod() #give error

# print("saalry",Steve.method1())
# print("Salary:", Steve.__salary)  # this will cause an error
print(Steve._Employee__privatemethod())  # accessing a private property
