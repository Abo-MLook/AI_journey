list1 = [100, 200, 300]
print(list1)
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


list1 = [1,2,3]
list1 += [3,4,5]
print(list1)
list1[3] = 4
print(list1)
