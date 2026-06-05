d1 = {'a': 5, 'b': 8, 'c':9}
d2 = {'a': 7, 'b': 6, 'c':4}
kaysd = d1.keys()

d3 = {}

for key in kaysd:
    d3[key]= max(d1[key],d2[key])


print(d3)