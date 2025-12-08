import pandas as pd

df = pd.DataFrame({
    'Math': [90, 70],
    'Science': [85, 95]
}, index=['Ali', 'Sara'])

print(df)
print()
stacked = df.stack()
print(stacked)
print()

unstacked = stacked.unstack()
print(unstacked)
print()
print(unstacked.unstack())
print()
print(unstacked.unstack().unstack())


"""
This example illustrates the `stack()` and `unstack()` reshaping operations in pandas.

- `stack()` pivots column labels into a new inner row index, producing a Series with a 
  MultiIndex. Each row–column combination becomes its own entry.

- `unstack()` performs the reverse operation: it takes the inner index level and pivots 
  it back into columns, reconstructing the original DataFrame layout.

These two operations allow flexible reshaping between wide and long formats, useful for 
tidy data transformations and multi-dimensional analysis.
"""


