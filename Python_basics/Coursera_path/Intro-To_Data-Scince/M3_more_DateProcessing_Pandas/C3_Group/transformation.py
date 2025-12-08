import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'cancellation_policy': ['strict', 'flexible', 'strict', 'flexible', 'strict'],
    'review_scores_value': [4.5, 4.7, 3.8, 4.9, 4.3]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print()
# Grouping by 'cancellation_policy' and calculating mean of 'review_scores_value' per group using transform
cols = ['cancellation_policy', 'review_scores_value']
transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)

# Display the transformed DataFrame
print("\nDataFrame After Transformation:")
print(transform_df)
