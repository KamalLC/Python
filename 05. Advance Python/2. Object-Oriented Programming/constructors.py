class MyClass:
    x = 5  # class variable/attribute
    y = 10 # class variable

    def __init__(self,a): #self = a, a = 5, b = 6
        self.a = a  #instance variable   #a.a = 5
        self.b = a  #instance variable   #a.b = 6
    
    def my_method(self):
        print("Hello World")
    
    def my_method_2(self, num):
        print(num)
    
    def add_numbers(self, a, b):
        return a + b
    
    def print_vars(self):
        print(self.a)
        print(self.b)

    def change_a(self, a):
        self.a = a
        print(self.a)

a = MyClass(5) #a = MyClass.__init__(a)
a.change_a(8)
a.print_vars()

# obj1 = MyClass(10, 20) #=> MyClass.__init__(obj1, 10, 20)
# print(obj1.a)
# print(obj1.b)

# obj1.print_vars()