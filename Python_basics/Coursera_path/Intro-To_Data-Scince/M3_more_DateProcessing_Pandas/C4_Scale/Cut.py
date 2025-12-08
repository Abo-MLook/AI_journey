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
