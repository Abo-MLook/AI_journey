my_str = "MICHIGAN"
for c in my_str:
    print(c,end = "\n")


## concate and reapeat:
fruit = ["apple","orange","banana","cherry"]
print([1,2] + [3,4])
print(fruit+[6,7,8,9])

print([0] * 4)


a = "I have had an apple on my desk before!"
print(a.count("e"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.index("electron"))
#print(z.index("da")) # error not in list

qu = "wow, welcome week!"
ty = qu.index("we")
print(ty)
ty1 = qu.count("we")
print(ty1)


song = "The rain in Spain..."
wds = song.split()
print(wds) # split reutrn a list



wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))