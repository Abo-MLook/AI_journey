import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df=pd.read_csv("census.csv")
# Sometimes it is useful to represent categorical values as each being a column with a true or a false as to
# whether the category applies. This is especially common in feature extraction, which is a topic in the data
# mining course. Variables with a boolean value are typically called dummy variables, and pandas has a built
# in function called get_dummies which will convert the values of a single column into multiple columns of
# zeros and ones indicating the presence of the dummy variable. I rarely use it, but when I do it's very
# handy.

# There’s one more common scale-based operation I’d like to talk about, and that’s on converting a scale from
# something that is on the interval or ratio scale, like a numeric grade, into one which is categorical. Now,
# this might seem a bit counter intuitive to you, since you are losing information about the value. But it’s
# commonly done in a couple of places. For instance, if you are visualizing the frequencies of categories,
# this can be an extremely useful approach, and histograms are regularly used with converted interval or ratio
# data. In addition, if you’re using a machine learning classification approach on data, you need to be using
# categorical data, so reducing dimensionality may be useful just to apply a given technique. Pandas has a
# function called cut which takes as an argument some array-like structure like a column of a dataframe or a
# series. It also takes a number of bins to be used, and all bins are kept at equal spacing.

# Lets go back to our census data for an example. We saw that we could group by state, then aggregate to get a
# list of the average county size by state. If we further apply cut to this with, say, ten bins, we can see
# the states listed as categoricals using the average county size.

# And we reduce this to country data
df=df[df['SUMLEV']==50]

# And for a few groups
df=df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average)

print(df.head())
print()
# Now if we just want to make "bins" of each of these, we can use cut()
print(pd.cut(df,10).head())
# make intereval that a mean in with 10 interval
# Here we see that states like alabama and alaska fall into the same category, while california and the
# disctrict of columbia fall in a very different category.

# Now, cutting is just one way to build categories from your data, and there are many other methods. For
# instance, cut gives you interval data, where the spacing between each category is equal sized. But sometimes
# you want to form categories based on frequency – you want the number of items in each bin to the be the
# same, instead of the spacing between bins. It really depends on what the shape of your data is, and what
# you’re planning to do with it.



"""
This code shows two common techniques for converting categorical or numeric data into 
useful feature representations: dummy variables and binning with `cut()`.

Dummy Variables:
- `get_dummies()` converts a categorical column into multiple boolean (0/1) columns.
- This is often used in feature engineering for machine learning models that require 
  numerical inputs.

Binning Numeric Data with `cut()`:
- After filtering the census dataset to county-level records, average county population 
  per state is computed.
- `pd.cut(df, 10)` divides these numeric averages into 10 equal-width intervals.
- Each state is assigned to an interval (bin), producing categorical labels that group 
  states by population scale.

Conceptual notes:
- `cut()` creates interval-based categories with equal spacing between bins.
- If equal *frequency* bins are desired instead, other methods (like `qcut`) may be used.
- Binning reduces continuous data into categorical groups, simplifying visualization and 
  enabling certain machine learning workflows.

Overall, dummy variables and binning are fundamental tools in feature extraction and 
categorizing continuous variables for analysis or modeling.
"""
