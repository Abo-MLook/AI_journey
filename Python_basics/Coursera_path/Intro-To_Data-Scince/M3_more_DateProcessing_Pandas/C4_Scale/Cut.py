import pandas as pd

# Create a DataFrame with ages
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [23, 35, 42, 50, 18]}

df = pd.DataFrame(data)

print(df)
print()
# Define the bins (intervals)
bins = [0, 30, 50, 100]

# Define the labels for the bins
labels = ['Young', 'Middle-aged', 'Old']

# Apply the cut function to create a new column for Age Group
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df)


"""
This code shows how to categorize continuous numeric data into labeled groups using 
`pd.cut()`.

How it works:

- Ages are placed into predefined bins:  
      [0–30], (30–50], (50–100]

- `labels` assigns human-readable names to each interval:
      'Young', 'Middle-aged', 'Old'

- `pd.cut(df['Age'], bins=bins, labels=labels)` returns a categorical Series where 
  each age is mapped to its corresponding age group.

The result is a new column, 'Age Group', that classifies each person by age range—useful 
for grouping, visualization, and analysis.
"""
