'''
The Series Datastructure
In this lecture we're going to explore the pandas Series structure.
By the end of this lecture you should be familiar with how to store and
manipulate single dimensional indexed data in the Series object.

The series is one of the core data structures in pandas. You think of it a cross
between a list and a dictionary. The items are all stored in an order and there's labels with
 which you can retrieve them. An easy way to visualize this is two columns of data. The first
 is the special index, a lot like keys in a dictionary. While the second is your actual data.
  It's important to note that the data column has a label of its own and can be retrieved using the .name attribute. This is different than with dictionaries and is useful when it comes to merging multiple columns of data. And we'll talk about that later on in the course.

'''


import pandas as  pd

# As you might expect, you can create a series by passing in a list of values.
# When you do this, Pandas automatically assigns an index starting with zero and
# sets the name of the series to None. Let's work on an example of this.

# One of the easiest ways to create a series is to use an array-like object, like
# a list.

# Here I'll make a list of the three of students, Alice, Jack, and Molly, all as strings
students = ['Alice', 'Jack', 'Molly']

# Now we just call the Series function in pandas and pass in the students
print(pd.Series(students))
print()


# The result is a Series object which is nicely rendered to the screen. We see here that
# the pandas has automatically identified the type of data in this Series as "object" and
# set the dytpe parameter as appropriate. We see that the values are indexed with integers,
# starting at zero
# We don't have to use strings. If we passed in a list of whole numbers, for instance,
# we could see that panda sets the type to int64. Underneath panda stores series values in a
# typed array using the Numpy library. This offers significant speedup when processing data
# versus traditional python lists.

# Let's create a little list of numbers
numbers = [1, 2, 3]
# And turn that into a series
print(pd.Series(numbers))
# And we see on my architecture that the result is a dtype of int64 objects

# There's some other typing details that exist for performance that are important to know.
# The most important is how Numpy and thus pandas handle missing data.

# In Python, we have the none type to indicate a lack of data. But what do we do if we want
# to have a typed list like we do in the series object?

# Underneath, pandas does some type conversion. If we create a list of strings and we have
# one element, a None type, pandas inserts it as a None and uses the type object for the
# underlying array.

# Let's recreate our list of students, but leave the last one as a None
students = ['Alice', 'Jack', None]
# And let's convert this to a series
print(pd.Series(students))
print()

# However, if we create a list of numbers, integers or floats, and put in the None type,
# pandas automatically converts this to a special floating point value designated as NaN,
# which stands for "Not a Number".

# So let's create a list with a None value in it
numbers = [1, 2, None]
# And turn that into a series
print(pd.Series(numbers))
print()


# You'll notice a couple of things. First, NaN is a different value. Second, pandas
# set the dytpe of this series to floating point numbers instead of object or ints. That's
# maybe a bit of a surprise - why not just leave this as an integer? Underneath, pandas
# represents NaN as a floating point number, and because integers can be typecast to
# floats, pandas went and converted our integers to floats. So when you're wondering why the
# list of integers you put into a Series is not floats, it's probably because there is some
# missing data.



# For those who might not have done scientific computing in Python before, it is important
# to stress that None and NaN might be being used by the data scientist in the same way, to
# denote missing data, but that underneath these are not represented by pandas in the same
# way.

# NaN is *NOT* equivilent to None and when we try the equality test, the result is False.

# Lets bring in numpy which allows us to generate an NaN value
import numpy as np
# And lets compare it to None
print(np.nan == None)
print()

# It turns out that you actually can't do an equality test of NAN to itself. When you do,
# the answer is always False.

print(np.nan == np.nan)
print()


# Instead, you need to use special functions to test for the presence of not a number,
# such as the Numpy library isnan().

print(np.isnan(np.nan))
print()
# So keep in mind when you see NaN, it's meaning is similar to None, but it's a
# numeric value and treated differently for efficiency reasons.