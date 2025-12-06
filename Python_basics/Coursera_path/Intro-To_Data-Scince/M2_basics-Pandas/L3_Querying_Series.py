# A pandas Series can be queried either by the index position or the index label. If you don't give an
# index to the series when querying, the position and the label are effectively the same values. To
# query by numeric location, starting at zero, use the iloc attribute. To query by the index label,
# you can use the loc attribute.
from logging import exception

# Lets start with an example. We'll use students enrolled in classes coming from a dictionary
import pandas as pd
students_classes = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'}
s = pd.Series(students_classes)
print(s)
print()



# So, for this series, if you wanted to see the fourth entry we would we would use the iloc
# attribute with the parameter 3.
print(s.iloc[3])
print()


# If you wanted to see what class Molly has, we would use the loc attribute with a parameter
# of Molly.
print(s.loc['Molly'])
print()



# Pandas tries to make our code a bit more readable and provides a sort of smart syntax using
# the indexing operator directly on the series itself. For instance, if you pass in an integer parameter,
# the operator will behave as if you want it to query via the iloc attribute
print(s[3])
print()


# If you pass in an object, it will query as if you wanted to use the label based loc attribute.
print(s['Molly'])
print()


# So what happens if your index is a list of integers? This is a bit complicated and Pandas can't
# determine automatically whether you're intending to query by index position or index label. So
# you need to be careful when using the indexing operator on the Series itself. The safer option
# is to be more explicit and use the iloc or loc attributes directly.

# Here's an example using class and their classcode information, where classes are indexed by
# classcodes, in the form of integers
class_code = {99: 'Physics',
              100: 'Chemistry',
              101: 'English',
              102: 'History'}
s = pd.Series(class_code)


# If we try and call s[0] we get a key error because there's no item in the classes list with
# an index of zero, instead we have to call iloc explicitly if we want the first item.
try:
    print(s[0])
except :
    print(f"error")
print()


# So, that didn't call s.iloc[0] underneath as one might expect, instead it
# generates an error