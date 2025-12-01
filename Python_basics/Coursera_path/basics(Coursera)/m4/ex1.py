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


a = [81,82,83]
a.remove(83)

print()
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
print(x)
print(y)
#   x += y (In-place modification):
#   x = x + y (Creates a new list)

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for word in wrds:
    past_wrds.append(word +"ed")
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
sc_list = scores.split()
a_scores = len(sc_list)
print(a_scores)
print()
p_phrase = "was it a car or a cat I saw"
p_rev = ""
p1_rev = p_phrase[::-1]

for char in p_phrase:
    p_rev = char + p_rev
print(p_rev)
print(p1_rev)

print(p_phrase ==p_rev)


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    ite = item.split(", ")
    print(f"The store has {ite[1]} {ite[0]}, each for {ite[2]}")
