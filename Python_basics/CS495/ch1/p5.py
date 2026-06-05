D = { 'name': {'first': 'Ali', 'last': 'Ahmed'},
'job': ['dev', 'mgr'],
'age': 40}

print(D['name'])
print(D['name']['first'])
print(D['job'][0])

D['job'].append('des')

print(D['job'])

age = {'Ali': 36, 'Ibrahim': 49, 'Saleh': 63, 'Fahad': 20, 'Sami': 77}
old = {name:age for name ,age in age.items() if age > 60}
print(old)