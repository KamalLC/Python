#creating a set
a = {1,2,3,3,4,5,5}
b = {4,'five',6}
c = {'seven',8,9.0}

# print(a[0]) #this will give error coz in set indexing is not supported
print(type(a))
l = [1,2,3,3,4,5,5]
s = set(l)
print(s)

s1 = set() #creating an empty set

# add, update set
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(3)
print(s1)

s1.update([4,5,6])
print(s1)

# s1.remove(14) #this will show error coz  14 is not there in the set s1
print(s1)

s1.discard(20) # 20 is not there in the set s1, even though this will not show any error
print(s1)

s1.pop()
print(s1)
# s1.clear()
# print(s1)

for ele in s1:
    print(ele)
