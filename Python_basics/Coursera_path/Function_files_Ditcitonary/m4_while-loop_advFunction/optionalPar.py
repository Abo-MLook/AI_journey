print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base -> convret 100 to base 10
print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64 -> convret 100 to base 8


def f(x):
    return x - 1
print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))


list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem
print(tot)
acc = 0
tot = 0
while acc < len(list1):
    tot+=list1[acc]
    acc +=1
print(tot)


def sublist(lis: list) -> list:
    index = 0
    rlist = []
    while index < len(lis):
        if lis[index] == 5:
            break
        rlist.append(lis[index])
        index += 1
    return rlist


