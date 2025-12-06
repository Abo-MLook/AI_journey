import pandas as pd

# One last note on using the indexing operators to access series data. The .loc attribute lets
# you not only modify data in place, but also add new data as well. If the value you pass in as
# the index doesn't exist, then a new entry is added. And keep in mind, indices can have mixed types.
# While it's important to be aware of the typing going on underneath, Pandas will automatically
# change the underlying NumPy types as appropriate.

# Here's an example using a Series of a few numbers.
s = pd.Series([1, 2, 3])

# We could add some new value, maybe a university course
s.loc['History'] = 102

print(s)
print()


# We see that mixed types for data values or index labels are no problem for Pandas. Since
# "History" is not in the original list of indices, s.loc['History'] essentially creates a
# new element in the series, with the index named "History", and the value of 102


# Up until now I've shown only examples of a series where the index values were unique. I want
# to end this lecture by showing an example where index values are not unique, and this makes
# pandas Series a little different conceptually then, for instance, a relational database.

# Lets create a Series with students and the courses which they have taken
students_classes = pd.Series({'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'})
print(students_classes)
print()


# Now lets create a Series just for some new student Kelly, which lists all of the courses
# she has taken. We'll set the index to Kelly, and the data to be the names of courses.
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])
print(kelly_classes)
print()

# Finally, we can append all of the data in this new Series to the first using the .append()
# function.
all_students_classes = students_classes._append(kelly_classes)
students_classes._append(kelly_classes) # student clasees does not change
# This creates a series which has our original people in it as well as all of Kelly's courses
print(all_students_classes)
print()




# There are a couple of important considerations when using append. First, Pandas will take
# the series and try to infer the best data types to use. In this example, everything is a string,
# so there's no problems here. Second, the append method doesn't actually change the underlying Series
# objects, it instead returns a new series which is made up of the two appended together. This is
# a common pattern in pandas - by default returning a new object instead of modifying in place - and
# one you should come to expect. By printing the original series we can see that that series hasn't
# changed.
print(students_classes)
print()

# Finally, we see that when we query the appended series for Kelly, we don't get a single value,
# but a series itself.
print(all_students_classes.loc['Kelly'])
print()


"""
This part shows how .loc can be used to modify and add new values to a Series.

Key notes:
- .loc can update existing values and also create new entries if the label does not exist.
- A Pandas Series can contain mixed index types (numbers and strings together).
- Series indexes do NOT have to be unique.
- When duplicate indexes exist, selecting that label returns multiple values as a Series.
- Appending one Series to another creates a NEW Series and does NOT modify the original.
- After append, the original Series remains unchanged.
"""
