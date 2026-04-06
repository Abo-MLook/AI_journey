"""
Querying DataFrame
In this lecture we're going to talk about querying DataFrames.
The first step in the process is to understand Boolean masking.
 Boolean masking is the heart of fast and efficient querying in numpy and pandas,
 and it's analogous to bit masking used in other areas of computational science.
 By the end of this lecture
you'll understand how Boolean masking works, and how to apply this to a DataFrame
to get out data you're interested in.

A Boolean mask is an array which can be of one dimension like a series,
 or two dimensions like a data frame, where each of the values in the array are either true
 or false. This array is essentially overlaid on top of the data structure that we're querying.
  And any cell aligned with the true value will be admitted into our final result,
  and any cell aligned with a false value will not.
"""


# Let's start with an example and import our graduate admission dataset. First we'll bring in pandas
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# Then we'll load in our CSV file
df = pd.read_csv('Admission_Predict.csv', index_col=0)
# And we'll clean up a couple of poorly named columns like we did in a previous lecture
df.columns = [x.lower().strip() for x in df.columns]
# And we'll take a look at the results
print(df.head())


# Boolean masks are created by applying operators directly to the pandas Series or DataFrame objects.
# For instance, in our graduate admission dataset, we might be interested in seeing only those students
# that have a chance higher than 0.7

# To build a Boolean mask for this query, we want to project the chance of admit column using the
# indexing operator and apply the greater than operator with a comparison value of 0.7. This is
# essentially broadcasting a comparison operator, greater than, with the results being returned as
# a Boolean Series. The resultant Series is indexed where the value of each cell is either True or False
# depending on whether a student has a chance of admit higher than 0.7
ad_mask = df["chance of admit"] > 0.7
print()
# So, what do you do with the boolean mask once you have formed it? Well, you can just lay it on top of the
# data to "hide" the data you don't want, which is represented by all of the False values. We do this by using
# the .where() function on the original DataFrame.
print(df.where(ad_mask).dropna().head())
# We see that the resulting data frame keeps the original indexed values, and only data which met
# the condition was retained. All of the rows which did not meet the condition have NaN data instead,
# but these rows were not dropped from our dataset.
#
# The next step is, if we don't want the NaN data, we use the dropna() function
print()
print(df[ad_mask].head())

print()

# I personally find this much harder to read, but it's also very more common when you're reading other
# people's code, so it's important to be able to understand it. Just reviewing this indexing operator on
# DataFrame, it now does two things:

# It can be called with a string parameter to project a single column
print(df["gre score"].head()) # return a series because one columns
print()
print(df[["gre score","toefl score"]].head()) # return a DataFrame because more then one columns

# gre score>320 ?

print()
msk = df["gre score"] > 320
print(df[msk].head())
print()
#or
print(df[df["gre score"] > 320].head())
print()
# And each of these is mimicing functionality from either .loc() or .where().dropna().


# Before we leave this, lets talk about combining multiple boolean masks, such as multiple criteria for
# including. In bitmasking in other places in computer science this is done with "and", if both masks must be
# True for a True value to be in the final mask), or "or" if only one needs to be True.

# Unfortunatly, it doesn't feel quite as natural in pandas. For instance, if you want to take two boolean
# series and and them together
try:
    twomsk = (df['chance of admit'] > 0.7) and (df['chance of admit'] < 0.9)
except:
    print("you should use & insted of and")

# This doesn't work. And despite using pandas for awhile, I still find I regularly try and do this. The
# problem is that you have series objects, and python underneath doesn't know how to compare two series using
# and or or. Instead, the pandas authors have overwritten the pipe | and ampersand & operators to handle this
# for us
twomsk = (df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)
print(df[twomsk].head())
print()

try:
    twomsk = df['chance of admit'] > 0.7 & df['chance of admit'] < 0.9
except:
    print("you should use gt and lt insted of < or >")


twomsk = df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9)
print(df[twomsk].head)

#or and best
twomsk = df['chance of admit'].gt(0.7).lt(0.9)
# This only works if you operator, such as less than or greater than, is built into the DataFrame, but I
# certainly find that last code example much more readable than one with ampersands and parenthesis.


"""
This part explains how to filter (query) a DataFrame using Boolean masking.

Key notes:
- Boolean masking creates a True/False filter based on a condition.
- Example: df["chance of admit"] > 0.7 returns a boolean Series.
- You can filter rows directly using:
  → df[mask]
- df.where(mask) keeps original shape but fills False rows with NaN.
- df[mask] is cleaner because it removes unwanted rows directly.
- The indexing operator [] does:
  → Column selection if passed a string
  → Row filtering if passed a boolean mask
- To combine conditions:
  → Use & for AND
  → Use | for OR
  → NEVER use and / or with Series
- Always wrap each condition in parentheses when using & or |.
- You can use .gt(), .lt(), etc. for clearer chained comparisons.

This is the main tool for fast filtering and searching in Pandas.
"""
