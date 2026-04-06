import pandas as pd

# Let's talk more about how pandas' Series can be created. While my list might be a common
# way to create some play data, often you have label data that you want to manipulate.
# A series can be created directly from dictionary data. If you do this, the index is
# automatically assigned to the keys of the dictionary that you provided and not just
# incrementing integers.

# Here's an example using some data of students and their classes.

students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
s = pd.Series(students_scores)
print(s)
print()
# We see that, since it was string data, pandas set the data type of the series to "object".
# We see that the index, the first column, is also a list of strings.

# Once the series has been created, we can get the index object using the index attribute.
print(s.index)
print()

# As you play more with pandas you'll notice that a lot of things are implemented as numpy
# arrays, and have the dtype value set. This is true of indicies, and here pandas infered
# that we were using objects for the index.

# Now, this is kind of interesting. The dtype of object is not just for strings, but for
# arbitrary objects. Lets create a more complex type of data, say, a list of tuples.
students = [("Alice","Brown"), ("Jack", "White"), ("Molly", "Green")]
print(pd.Series(students))
print()

# We see that each of the tuples is stored in the series object, and the type is object.

# You can also separate your index creation from the data by passing in the index as a
# list explicitly to the series.

s = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack', 'Molly'])
print(s)
print()

# So what happens if your list of values in the index object are not aligned with the keys
# in your dictionary for creating the series? Well, pandas overrides the automatic creation
# to favor only and all of the indices values that you provided. So it will ignore from your
# dictionary all keys which are not in your index, and pandas will add None or NaN type values
# for any index value you provide, which is not in your dictionary key list.

# Here's and example. I'll pass in a dictionary of three items, in this case students and
# their courses
students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
# When I create the series object though I'll only ask for an index with three students, and
# I'll exclude Jack
s = pd.Series(students_scores, index=['Alice', 'Molly', 'Sam'])
print(s)
print()
# The result is that the Series object doesn't have Jack in it, even though he was in our
# original dataset, but it explicitly does have Sam in it as a missing value.



ste = {
"ID" : 1127846804,
"Name" : "Mrwan ALayed",
"Section":"CS",
"Level" : "8"
}
s = pd.Series(ste,index=["ID","Name","Section","Level","GPA"])
print(s)





"""
This part shows different ways to create a Pandas Series.

Key notes:
- A Series can be created from a dictionary, where:
  → Dictionary keys become the index.
  → Dictionary values become the data.
- The index of a Series can be accessed using .index.
- If the data contains mixed or complex types (like tuples), the dtype becomes "object".
- You can manually set the index when creating a Series using the index parameter.
- If the provided index does not match the dictionary keys:
  → Extra dictionary keys are ignored.
  → Missing index values are filled with NaN.
- This behavior is useful when you want full control over which labels appear in your data.
"""
