import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50] # I'll use the overloaded indexing operator [] which drops nans
# Update the dataframe to have a new index, we use inplace=True to do this in place
df.set_index(['STNAME','CTYNAME'], inplace=True)
# Set the column names
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
print(df.head())
print()
# Here's another pandas idiom. Python has a wonderful function called map, which is sort of a basis for
# functional programming in the language. When you want to use map in Python, you pass it some function you
# want called, and some iterable, like a list, that you want the function to be applied to. The results are
# that the function is called against each item in the list, and there's a resulting list of all of the
# evaluations of that function.

# Pandas has a similar function called applymap. In applymap, you provide some function which should operate
# on each cell of a DataFrame, and the return set is itself a DataFrame. Now I think applymap is fine, but I
# actually rarely use it. Instead, I find myself often wanting to map across all of the rows in a DataFrame.
# And pandas has a function that I use heavily there, called apply. Let's look at an example.
# Let's take a look at our census DataFrame. In this DataFrame, we have five columns for population estimates,
# with each column corresponding with one year of estimates. It's quite reasonable to want to create some new
# columns for minimum or maximum values, and the apply function is an easy way to do this.

# First, we need to write a function which takes in a particular row of data, finds a minimum and maximum
# values, and returns a new row of data nd returns a new row of data.  We'll call this function min_max, this
# is pretty straight forward. We can create some small slice of a row by projecting the population columns.
# Then use the NumPy min and max functions, and create a new series with a label values represent the new
# values we want to apply.

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

# Then we just need to call apply on the DataFrame.

# Apply takes the function and the axis on which to operate as parameters. Now, we have to be a bit careful,
# we've talked about axis zero being the rows of the DataFrame in the past. But this parameter is really the
# parameter of the index to use. So, to apply across all rows, which is applying on all columns, you pass axis
# equal to 'columns'.
print(df.apply(min_max, axis='columns').head())
# Here's an example where we have a revised version of the function min_max Instead of returning a separate
# series to display the min and max we add two new columns in the original dataframe to store min and max

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    # Create a new entry for max
    row['max'] = np.max(data)
    # Create a new entry for min
    row['min'] = np.min(data)
    return row
# Now just apply the function across the dataframe
print(df.apply(min_max, axis='columns'))
print()

# Apply is an extremely important tool in your toolkit. The reason I introduced apply here is because you
# rarely see it used with large function definitions, like we did. Instead, you typically see it used with
# lambdas. To get the most of the discussions you'll see online, you're going to need to know how to at least
# read lambdas.

# Here's You can imagine how you might chain several apply calls with lambdas together to create a readable
# yet succinct data manipulation script. One line example of how you might calculate the max of the columns
# using the apply function.
rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014',
'POPESTIMATE2015']
# Now we'll just apply this across the dataframe with a lambda
print(df.apply(lambda x: np.max(x[rows]), axis=1).head())
print()

# The beauty of the apply function is that it allows flexibility in doing whatever manipulation that you
# desire, as the function you pass into apply can be any customized however you want. Let's say we want to
# divide the states into four categories: Northeast, Midwest, South, and West We can write a customized
# function that returns the region based on the state the state regions information is obtained from Wikipedia

def get_state_region(x):
    northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire',
                 'Rhode Island', 'Vermont', 'New York', 'New Jersey', 'Pennsylvania']
    midwest = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa',
               'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota',
               'South Dakota']
    south = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina',
             'South Carolina', 'Virginia', 'District of Columbia', 'West Virginia',
             'Alabama', 'Kentucky', 'Mississippi', 'Tennessee', 'Arkansas',
             'Louisiana', 'Oklahoma', 'Texas']
    west = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah',
            'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']

    if x in northeast:
        return "Northeast"
    elif x in midwest:
        return "Midwest"
    elif x in south:
        return "South"
    else:
        return "West"

# Now we have the customized function, let's say we want to create a new column called Region, which shows the
# state's region, we can use the customized function and the apply function to do so. The customized function
# is supposed to work on the state name column STNAME. So we will set the apply function on the state name
# column and pass the customized function into the apply function
df['state_region'] = df['STNAME'].apply(lambda x: get_state_region(x))
print(df[['STNAME','state_region']].head())

"""
This code demonstrates how to use pandas `apply()` to perform row-wise computations, 
create new columns, and apply custom logic to a DataFrame.

Key ideas:

- After loading and filtering the census data, several yearly population estimate 
  columns are used to compute row-level min/max values.  
    df.apply(min_max, axis='columns')

- `apply()` passes each row to a function when `axis='columns'`, allowing flexible 
  operations such as inserting new fields (`min`, `max`) back into the row.

- Lambdas provide concise inline transformations:  
    df.apply(lambda x: np.max(x[rows]), axis=1)

- A custom function (`get_state_region`) classifies states into regions, and `apply()` 
  is used to map state names into a new categorical column:
    df['state_region'] = df['STNAME'].apply(lambda x: get_state_region(x))

Overall, `apply()` is a versatile pandas tool for custom row/column operations, 
numeric transformations, and feature creation.
"""
