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
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.reverse()
print(winners)


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = (sorted(medals.keys() , key= lambda k:medals[k]))[:-4:-1]
print(top_three)

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

# Sorting the keys based on their values in descending order
most_needed = sorted(groceries.keys(), key=lambda k: groceries[k], reverse=True)

print(most_needed)