# Let's bring in pandas as normal
import pandas as pd

# Here’s an example. Lets create a dataframe of letter grades in descending order. We can also set an index
# value and here we'll just make it some human judgement of how good a student was, like "excellent" or "good"

df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good',
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])
print(df)
print()
# Now, if we check the datatype of this column, we see that it's just an object, since we set string values
print(df.dtypes)
print()

# We can, however, tell pandas that we want to change the type to category, using the astype() function
print(df["Grades"].astype("category").head())
print()

# We see now that there are eleven categories, and pandas is aware of what those categories are. More
# interesting though is that our data isn't just categorical, but that it's ordered. That is, an A- comes
# after a B+, and B comes before a B+. We can tell pandas that the data is ordered by first creating a new
# categorical data type with the list of the categories (in order) and the ordered=True flag
my_categories=pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                           ordered=True)
# then we can just pass this to the astype() function
grades=df["Grades"].astype(my_categories)
print(grades.head())
print()


print(df[df["Grades"]>"C"])
print()
# So a C+ is great than a C, but a C- and D certainly are not. However, if we broadcast over the dataframe
# which has the type set to an ordered categorical

print(grades[grades>"C"])
# We see that the operator works as we would expect. We can then use a certain set of mathematical operators,
# like minimum, maximum, etc., on the ordinal data.


"""
This code demonstrates how to use pandas categorical data types—especially *ordered* 
categories—to work with graded or ranked values.

Key ideas:

- A DataFrame of letter grades is created, and the 'Grades' column is initially of type 
  object (string).

- Converting to a categorical type:
      df["Grades"].astype("category")
  makes pandas store the values efficiently but does not yet give them an order.

- To define a meaningful order (D < C- < C < ... < A+), a `CategoricalDtype` is created 
  with an explicit category list and `ordered=True`.

- Converting with:
      grades = df["Grades"].astype(my_categories)
  allows comparisons such as `grades > "C"` to behave correctly based on grade ranking.

- Ordered categorical types also support operations like min, max, and sorting according 
  to the defined order.

Overall, ordered categoricals provide a powerful way to handle ranked qualitative data 
such as grades, satisfaction levels, or survey responses.
"""
