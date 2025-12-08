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

