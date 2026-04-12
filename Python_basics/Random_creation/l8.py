List3 = [[1,2,3], [4,5,6], [7,8,9]]
print(List3[1][1])

print()
print([x[1] for x in List3])
print([x[1] for x in List3 if x[1] != 2])


L1 = [12, -16, 0, 23, -57, -33, 92, -46, 83]
L2 = [i + 100 for i in L1 if i<0]
print(L2)





def largest_number1(lst:list[int]):
    max = lst[0] +  lst[1]
    for i in range(len(lst)):
        for j in range( i + 1 , len(lst)):
            if max < lst[i] +  lst[j]:
                max =lst[i] +  lst[j]