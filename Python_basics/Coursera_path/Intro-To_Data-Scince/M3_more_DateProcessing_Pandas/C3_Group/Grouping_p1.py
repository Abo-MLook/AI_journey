# Let's look at an example. First, we'll bring in our pandas and numpy libraries
import pandas as pd
import numpy as np

# Let's look at some US census data
df = pd.read_csv('census.csv')
# And exclude state level summarizations, which have sum level value of 40
df = df[df['SUMLEV']==50]
print(df.head())
print(df.groupby('STNAME').head())

