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