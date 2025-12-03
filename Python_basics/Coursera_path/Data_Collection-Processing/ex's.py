nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = None
if "data" in nested.keys():
    data = True
else:
    data = False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = None
if 24 in nested["data"]:
    twentyfour = True
else:
    twentyfour = False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = None
if 'whole' in nested["window"]:
    whole = False
else:
    whole = True
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = None
if "data" in nested.keys():
    physics = True
else:
    physics = False

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22, 'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29, 'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20, 'Germany': 13}}

US_count = []

for nes_dic in nested_d.keys():
    US_count.append(nested_d[nes_dic]['USA'])
print(US_count)



l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for nes_dic in l_of_l:
    print(nes_dic)
    third.append(nes_dic[2])
print(third)