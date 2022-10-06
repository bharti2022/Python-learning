class Employee:

    # method overloading || instance method
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)


# cerating an object of the Employee class
Steve = Employee()
# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")
print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")
print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)