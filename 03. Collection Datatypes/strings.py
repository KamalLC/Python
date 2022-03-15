# example below show that list is mutable and 
# string is immutable
# try to visualize difference in string concatenation and list concatenation

a="kamal"
print(id(a)) 
a+=" lamichhane"
print(id(a)) #this is different from above id

li=[2, 3, 4]
print(f'li first={id(li)}')
li+=[1, 2, 3]
print(f'li second={id(li)}') # this is same as above id

#creating a string
a = 'hello'
b = "hello"
c = 'Don\'t worry \t \t about apostrophes\n'
f = '''This is a long string that is made up of
               several lines and non-printable characters
        such as tabs and line feeds, etc. 
        '''
print(a)
print(b)
print(c)
print(f)

#accessing elements/characters in a string

a = 'hello'
print(a[0])
print(a[4])

#negative indexing
print(a[-1])
print(a[-2])

#slicing a string
print(a[0:2])
print(a[:])

#a[0] = 'H' #this will show error coz string is immutable
print(a)

#del a[0] #this will show error coz string is immutable
print(a)
del a
# print(a) #this will show error coz string a is already deleted


for ele in c:
    print(ele)

#check if string is in a string
s = 'hello'
print('H' not in s) #True

c = 'hello\\world' # \ is escape operator
print(c)


#string methods
# format()
a = 'hello'
b = 'world'
print(a, b)
print('{} {}'.format(a,b))
print('{1} {0} {1}'.format(a,b))
print(f'{a} is the  {b} {a}')