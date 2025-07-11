# recursive function to print 1 to 10
def counter(num = 1):
    if num > 10:
        return
    print(num , end=" ")
    counter(num + 1)
counter()
print()

# recursive function to print 1 to 10 inversely parameter should start from 1

def Incounter(num =1):
    if num < 10:
        Incounter(num + 1)
    print(num , end=" ")
    return

Incounter()

print()
# recursive function to add 1 to 10

def addtion(num = 1):
    if num == 10:
        return num
    return num + addtion(num + 1)

print(addtion())


# recursive function to add n to 1

def addtion2(num):
    if num == 1:
        return 1
    return num + addtion2(num - 1)

number = int(input("Enter a number to cal the addtion to 1 :"))
print(addtion2(number))
