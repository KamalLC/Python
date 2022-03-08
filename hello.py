print("Hello World")

# variables
a=1
b=3.15

c="Kamal Lamichhane"
d=True

# type function returns the type of parameter passed
print(type(c))

# input function takes input from the user
# string in the parenthesis is displayed as it is in the console
x=input("Enter a number: ")
print(f'The number you entered is {x}')

#type conversion
sum=a+b # a is converted to float implicitely then the addition of two float numbers is done
print(sum)

# explicit type conversion
num="112" #string
print(type(num))
num=int(num) # explicit conversion of string to int
print(type(num))


# arithmetic operators
j=7
k=3
print(f'Sum= {j+k}') # addition
print(f'Difference= {j-k}') #subtraction
print(f'product={j*k}') #multiplication
print(f'j^k={j**k}') #power
print(f'division= {j/k}') #division in float
print(f'floor division= {j//k}') #floor division
print(f'remainder= {j%k}') #modulus operator

#string operations
a="Kamal "
b="Lamichhane"
print(a+b) #string concatenation
print(a*5) #multiplicaion

# types of assignment operator
j+=k
j-=k
j*=k
j/=k
j%=k
r=5
r%=3
print(r)