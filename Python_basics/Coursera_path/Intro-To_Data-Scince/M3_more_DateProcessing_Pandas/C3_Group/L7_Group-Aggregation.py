'''
o this point we have applied very simple processing to our data after splitting,
really just outputting some print statements to demonstrate how the splitting works.
The pandas developers have three broad categories of data processing to happen during the apply step,
Aggregation of group data, Transformation of group data, and Filtration of group data
'''

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df=pd.read_csv("listings.csv")
# The most straight forward apply step is the aggregation of data, and uses the method agg() on the groupby
# object. Thus far we have only iterated through the groupby object, unpacking it into a label (the group
# name) and a dataframe. But with agg we can pass in a dictionary of the columns we are interested in
# aggregating along with the function we are looking to apply to aggregate.
# Now lets group by the cancellation policy and find the average review_scores_value by group
print(df.groupby("cancellation_policy").agg({"review_scores_value":np.average}))
print()
# Hrm. That didn't seem to work at all. Just a bunch of not a numbers. The issue is actually in the function
# that we sent to aggregate. np.average does not ignore nans! However, there is a function we can use for this
print(df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean}))
#print(df.groupby("cancellation_policy").agg({"review_scores_value": "mean"}))
print()
# We can just extend this dictionary to aggregate by multiple functions or multiple columns.
print(df.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd),
                                      "reviews_per_month":np.nanmean}))
print(df.groupby("cancellation_policy").agg({
    "review_scores_value": ["mean", "std"],  # Use strings "mean" and "std"
    "reviews_per_month": "mean"              # Mean of 'reviews_per_month'
}))
# Take a moment to make sure you understand the previous cell, since it's somewhat complex. First we're doing
# a group by on the dataframe object by the column "cancellation_policy". This creates a new GroupBy object.
# Then we are invoking the agg() function on that object. The agg function is going to apply one or more
# functions we specify to the group dataframes and return a single row per dataframe/group. When we called
# this function we sent it two dictionary entries, each with the key indicating which column we wanted
# functions applied to. For the first column we actually supplied a tuple of two functions. Note that these
# are not function invocations, like np.nanmean(), or function names, like "nanmean" they are references to
# functions which will return single values. The groupby object will recognize the tuple and call each
# function in order on the same column. The results will be in a heirarchical index, but since they are
# columns they don't show as an index per se. Then we indicated another column and a single function we wanted
# to run.