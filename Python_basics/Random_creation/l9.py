from Python_basics.basics2.L11_scope.scope import count


def f1():
	print("You are in function 1")
def f2():
	print("You are in function 2")
f1()
f2()
f2 = f1
a = f1
f2()
def multiply(x =1, y:int  = 10):
	  return x * y


print(multiply("mr",3))



def matching(n1:str , n2:str):
    matcing = []
    n1 = n1.lower()
    n2 = n2.lower()
    l = len(n1) if len(n1)<len(n2) else len(n2)
    for i in range(l):
        if n1[i] == n2[i]:
            matcing.append(n1[i])




    return matcing


print(matching("MRWAN","rawan"))


print("name".count("n"))


print(("a" in "name"))

def maxe(*numbers):
    print(numbers)
    return max(numbers)


print(maxe(1,2,3,4))


def largest_number(lst:list[int]):

    return max(lst)


print(largest_number([10, 5, 20, 8]))  # 20