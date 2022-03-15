#__name__ attribute returns the name of the module
import math
import my_module as m
# print(dir(math))
# print(dir(my_module))
print(math.__name__)
print(m.__name__)

print("__name__ = ", __name__)
print(type(__name__))