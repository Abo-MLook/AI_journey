import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df=pd.read_csv("listings.csv")


# For instance, suppose we want to include the average rating values in a given group by cancellation policy,
# but preserve the dataframe shape so that we could generate a difference between an individual observation
# and the sum.

# First, lets define just some subset of columns we are interested in
cols=['cancellation_policy','review_scores_value']
# Now lets transform it, I'll store this in its own dataframe
transform_df=df[cols].groupby('cancellation_policy').transform(np.nanmean)
print(df[cols].head())
print()

print(transform_df.head())

# So we can see that the index here is actually the same as the original dataframe. So lets just join this
# in. Before we do that, lets rename the column in the transformed version
transform_df.rename({'review_scores_value':'mean_review_scores'}, axis='columns', inplace=True)
df=df.merge(transform_df, left_index=True, right_index=True)
print(df.head())
print()

# Great, we can see that our new column is in place, the mean_review_scores. So now we could create, for
# instance, the difference between a given row and it's group (the cancellation policy) means. X - mean
df['mean_diff']=np.absolute(df['review_scores_value']-df['mean_review_scores'])
print(df['mean_diff'].head())
print()


"""
This code demonstrates *group-wise transformation* using `groupby().transform()`, 
which differs from aggregation by preserving the original DataFrame’s shape.

Key ideas:

- A subset of columns is selected: ['cancellation_policy', 'review_scores_value'].

- `transform(np.nanmean)` computes the mean review score *within each cancellation 
  policy group*, but returns a Series/DataFrame with the **same index** as the original.
    transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)

- Because the shape and index are preserved, the transformed values can be merged 
  back into the original DataFrame as new columns.

- The transformed column is renamed to 'mean_review_scores' before merging.

- Once the per-group mean is available for every row, additional row-level 
  calculations become easy—for example, the deviation of each listing’s rating 
  from its group mean:
    df['mean_diff'] = |review_scores_value − mean_review_scores|

Summary:
`transform()` applies a function per group but returns results aligned with the 
original rows, making it ideal for feature engineering such as computing 
normalized values, group deviations, z-scores, or percent differences.
"""
