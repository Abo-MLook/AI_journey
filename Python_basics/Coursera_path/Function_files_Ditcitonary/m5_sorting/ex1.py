lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst,reverse=True)
print(lst_sorted)
print()

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))
