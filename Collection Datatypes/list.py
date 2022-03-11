a = [1, 2, 3]
b = [4, 'five', 6.0]
c = ['seven', 8, 9.0,[10,11,12]]
d = []


# negative indexing
print(a[-1])
print(b[-2])
print(c[-1][-1])

#slicing a list
print(a[0:2]) 
print(a[:]) 
print(b[1:])  
print(c[3][1:3])

#change items of a list
a[0] = 'one'
print(a)

a = [1, 2, 3]
a.append(4)  #append adds an element to the end of the list, only one element
print(a)


new = [11,22,33]
a.extend(new) #extend adds a list to the end of the list, multiple elements
print(a)


f = [1,2,3]
g = [4,5,6]
h = f + g
print(h)


d = [1,2,3]
d.insert(1,4) #insert adds an element at a specific index
print(d)

#remove elements from a list
mylist = [1,2,3,4,5,6,7,8,9,10]
del mylist[0]
print(mylist)

mylist.remove(5) 
print(mylist)


mylist.pop() #pop removes the last element of the list
print(mylist)

mylist.pop(0) #pop removes the element at a specific index
print(mylist)


mylist.clear() #clear removes all elements from the list
print(mylist)



# #list copy
list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)
print(list1 is list2) #True because list1 and list2 point to the same list

#another way to copy a list
list1 = [1,2,3]
list2 = list1.copy()
print(list1)
print(list2)
print(f'here: {list1 is list2}') #False because list1 and list2 do not point to the same list
print(f'here: {list1 == list2}')


#loop through a list
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    print(i)

# membership operator
print(1 in mylist) #True
print(11 in mylist) #False

#Note: assignment operator to copy list makes new variable to point to original list
a = [1,2,3]
print(a)
print(id(a))

b = a
print(b)
print(id(b))

a[0] = 4
print(a)
print(b)
print(a==b)
print(a is b)
