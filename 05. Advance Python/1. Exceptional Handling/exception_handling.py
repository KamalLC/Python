if 5 > 3:  # Syntax Error
    print("Hello") 

# a = 5
# print(b)  # Name Error

#print(5/0)  # ZeroDivisionError
#print(math.pi) # ImportError

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

x='a'

print(5-x)