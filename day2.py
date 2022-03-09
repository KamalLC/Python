# if statements

x=5

if x>0:
    print("x is positive")


# if else

if x%2==0:
    print("x is even")
else:
    print("x is odd")


# if elif if
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("zero")


#nested if else
if x%3==0:
    if x%2==0:
        print("even multiple of 3")
    else:
        print("odd multiple of 3")
else:
    print("not a multiple of 3")


# while loop
i=3
n=10
while i<=n:
    print(i)
    i+=1

#for loop
name="kamal Lamichhane"

for char in name:
    print(char)

#new thing that i learned
for char in name:
    print(char, end="") #prints the same string

#for loop in list(array)
num=[2, 4, 6]
for number in num:
    print(number)

# fizzbuzz with range()
for i in range(20):
    if i%3==0:
        if i%5==0:
            print("fizzbuzz")
        else:
            print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)