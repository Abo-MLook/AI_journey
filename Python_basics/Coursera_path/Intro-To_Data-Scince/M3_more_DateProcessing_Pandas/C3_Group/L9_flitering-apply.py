import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df=pd.read_csv("listings.csv")



# The GroupBy object has build in support for filtering groups as well. It's often that you'll want to group
# by some feature, then make some transformation to the groups, then drop certain groups as part of your
# cleaning routines. The filter() function takes in a function which it applies to each group dataframe and
# returns either a True or a False, depending upon whether that group should be included in the results.
# For instance, if we only want those groups which have a mean rating above 9 included in our results
print(df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)['review_scores_value'].head())
print()
# Notice that the results are still indexed, but that any of the results which were in a group with a mean
# review score of less than or equal to 9.2 were not copied over.


# By far the most common operation I invoke on groupby objects is the apply() function. This allows you to
# apply an arbitrary function to each group, and stitch the results back for each apply() into a single
# dataframe where the index is preserved.
# And lets just include some of the columns we were interested in previously
df=df[['cancellation_policy','review_scores_value']]
print(df.head())
print()

# In previous work we wanted to find the average review score of a listing and its deviation from the group
# mean. This was a two step process, first we used transform() on the groupby object and then we had to
# broadcast to create a new column. With apply() we could wrap this logic in one place
def calc_mean_review_scores(group):
    # group is a dataframe just of whatever we have grouped by, e.g. cancellation policy, so we can treat
    # this as the complete dataframe
    avg=np.nanmean(group["review_scores_value"])
    # now broadcast our formula and create a new column
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    return group

# Now just apply this to the groups
print(df.groupby('cancellation_policy').apply(calc_mean_review_scores).head())
# Using apply can be slower than using some of the specialized functions, especially agg(). But, if your
# dataframes are not huge, it's a solid general purpose approach

"""
Groupby is a powerful and commonly used tool for data cleaning and data analysis. Once you have grouped the data by some category you have a dataframe 
of just those values and you can conduct aggregated analysis on the segments that you are interested. The groupby() function follows a split-apply-combine 
approach - first the data is split into subgroups, then you can apply some transformation, filtering,
 or aggregation, then the results are combined automatically by pandas for us.
"""