import pandas as pd
import numpy as np

data = {
    'Student': ['Ali', 'Sara', 'Ali', 'Sara', 'Ali'],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math'],
    'Score': [90, 85, 88, 92, 95]
}

df = pd.DataFrame(data)
print(df)
print()
pivot = df.pivot_table(
    values='Score',      # what number we want to calculate
    index='Student',     # rows
    columns='Subject',   # columns
    aggfunc=np.mean      # how to summarize
)

print(pivot)

print()
print()

data = {
    'Class': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Subject': ['Math', 'Science', 'Math', 'Math', 'Science', 'Math'],
    'Score': [90, 85, 95, 88, 92, 91]
}

df = pd.DataFrame(data)
print(df)
print()
pivot = df.pivot_table(
    values='Score',
    index='Class',
    columns='Subject',
    aggfunc=np.mean
)

print(pivot)
print()

import pandas as pd
import numpy as np

data = {
    'Student': ['Ali', 'Ali', 'Ali', 'Sara', 'Sara', 'Sara'],
    'Subject': ['Math', 'Math', 'Science', 'Math', 'Science', 'Science'],
    'Score':   [80,    100,   90,        70,    95,        85]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

print()
pivot = df.pivot_table(
    values='Score',
    index='Student',
    columns='Subject',
    aggfunc=np.mean
)

print("\nPivot without margins:")
print(pivot)
print()

pivot_m = df.pivot_table(
    values='Score',
    index='Student',
    columns='Subject',
    aggfunc=np.mean,
    margins=True
)

print("\nPivot with margins=True:")
print(pivot_m)

print()