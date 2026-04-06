import pandas as pd

# Create a small DataFrame
data = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'C'],
    'Sales': [100, 200, 150, 250, 120, 220, 300],
    'Employees': [5, 10, 7, 8, 6, 9, 4]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print()
# Grouping by 'Store' and calculating the sum of sales for each store
grouped = df.groupby('Store')['Sales'].sum()

print("\nTotal Sales by Store:")
print(grouped)
print()

# Grouping by 'Store' and counting the number of entries (rows) for each store
store_counts = df.groupby('Store').size()

print("\nNumber of Entries by Store:")
print(store_counts)
print()

print(df)
print()
for item , group in df.groupby('Store'):
    print(group)
print()
for item , group in df.groupby('Store'):
    print(item)


"""
This code demonstrates the basics of grouping data in pandas using `groupby()`.

Key concepts:

- A simple DataFrame is created with store names, sales values, and employee counts.

- `groupby('Store')['Sales'].sum()` groups the rows by store and computes total sales 
  per store. This produces a Series with aggregated values.

- `groupby('Store').size()` counts how many rows belong to each store—useful for 
  understanding frequency or record counts.

- Iterating over `df.groupby('Store')` yields each store name and its corresponding 
  sub-DataFrame, allowing inspection or custom processing:
      for item, group in df.groupby('Store'):
          print(item)     # store label
          print(group)    # rows belonging to that store

Overall, `groupby()` provides powerful data summarization and segmentation, enabling 
aggregations and per-group operations in a clean, readable way.
"""
