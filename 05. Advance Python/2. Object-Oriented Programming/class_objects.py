class MyClass:
    x = 5 
    y = 10
    def my_method(self): #self = a
        print(self.x)  #a.x
        print(self.y)  #a.y
        print("Hello World")
    def hello(self,u): #self = a, u =5
        print(u)
    def add(self,i,o):
        return i+o


MyClass.x = 44
print(MyClass.x)

a = MyClass()  #object = instance
# #b = MyClass()
a.my_method()  #> MyClass.my_method(a)
a.hello(5)  #>MyClass.hello(a,5)
z = a.add(5,6) #>z = MyClass.add(a,5,6)
print(z)
print(a.x)
print(a.y)
a.my_method()

b  = MyClass()
print(b.x)
print(b.y)
b.my_method()

a.x = 50
b.x = 100

print(a.x)
print(b.x)


print(type(a))
a.hello(5)
x = 5
print(type(x))

l = [1,2,3,4,5]
l.append(6)
print(type(l))