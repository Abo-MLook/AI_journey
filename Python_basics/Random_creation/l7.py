list1 = [100,200,300]

list1.append(400)
print(list1)
list1.append([500, 600])
print(list1)

list1.extend([500, 600])
print(list1)

list1 += [700, 800]
print(list1)

list1.insert(1, 150)
print(list1)

list1[3:4] = [240, 280]
print(list1)


print(list1)
print()
print()


list1.pop(1) # take indix
print(list1)
list1.pop()
print(list1)
list1.remove(100) #take number
print(list1)
del list1[2]
print(list1)

list1.clear()

print(list1)