# Objects and refrences

# for a string it is the same object
a = "banana"
b = "banana"

print(a is b)
print(id(a))
print(id(b))

b = "a"
print(a)
b = a
b = "ba"
print(a)



# in list

a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))

print(a)
b = a
b[0] = 2
print(a)

print()
a = [81,82,83]
print(a)
b = a[:]
b[0] = 2
print(a)
print(b)

print()
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(0, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
mylist.pop(0)
mylist.pop()
print(lastitem)
print(mylist)