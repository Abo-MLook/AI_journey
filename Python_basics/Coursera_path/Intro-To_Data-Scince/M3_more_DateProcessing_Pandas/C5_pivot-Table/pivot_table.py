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


"""
This code demonstrates how to summarize data using `pivot_table()`, a powerful pandas 
tool for reshaping and aggregating data.

Core idea:
`pivot_table()` creates a new table where:
- `index` defines the rows,
- `columns` defines the columns,
- `values` is the data to aggregate,
- `aggfunc` specifies how to summarize (mean, sum, count, etc.).

Examples shown:

1. Student scores by subject:
      df.pivot_table(values='Score', index='Student', columns='Subject', aggfunc=np.mean)
   This computes each student's average score in each subject.

2. Class scores by subject:
   Same structure, but grouped by class instead of student.

3. Using `margins=True`:
   Adds row and column totals (labeled "All"), giving:
      - Overall mean per student,
      - Overall mean per subject,
      - Grand mean of all scores.

`pivot_table()` is essential for multi-dimensional summaries, making it easy to compare 
groups and compute aggregated statistics across several categories.
"""
