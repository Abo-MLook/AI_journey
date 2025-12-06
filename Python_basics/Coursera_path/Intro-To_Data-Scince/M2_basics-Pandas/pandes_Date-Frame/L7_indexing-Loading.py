# We see from the output that there is a list of columns, and the column identifiers are listed as strings on
# the first line of the file. Then we have rows of data, all columns separated by commas. Now, there are lots
# of oddities with the CSV file format, and there is no one agreed upon specification. So you should be
# prepared to do a bit of work when you pull down CSV files to explore. But this lecture isn't focused on CSV
# files, and is more about pandas DataFrames. So lets jump into that.

# Let's bring in pandas to work with
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Pandas mades it easy to turn a CSV into a dataframe, we just call read_csv()
df = pd.read_csv('Admission_Predict.csv')

# And let's look at the first few rows
print()
print(df.head())
print(df.columns)

print()
print()

# We notice that by default index starts with 0 while the students' serial number starts from 1. If you jump
# back to the CSV output you'll deduce that pandas has create a new index. Instead, we can set the serial no.
# as the index if we want to by using the index_col.
df = pd.read_csv('Admission_Predict.csv', index_col=0)
print(df.head())

print()
print()


# Notice that we have two columns "SOP" and "LOR" and probably not everyone knows what they mean So let's
# change our column names to make it more clear. In Pandas, we can use the rename() function It takes a
# parameter called columns, and we need to pass into a dictionary which the keys are the old column name and
# the value is the corresponding new column name
new_df=df.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
                   'University Rating':'University Rating',
                   'SOP': 'Statement of Purpose','LOR': 'Letter of Recommendation',
                   'CGPA':'CGPA', 'Research':'Research',
                   'Chance of Admit':'Chance of Admit'})
print(new_df.head())
print()

# If we look at the output closely, we can see that there is actually a space right after "LOR" and a space
# right after "Chance of Admit. Sneaky, huh? So this is why our rename dictionary does not work for LOR,
# because the key we used was just three characters, instead of "LOR "

# There are a couple of ways we could address this. One way would be to change a column by including the space
# in the name
new_df=new_df.rename(columns={'LOR ': 'Letter of Recommendation  '}) # put a new space
print(new_df.head())
print()
# So that works well, but it's a bit fragile. What if that was a tab instead of a space? Or two spaces?
# Another way is to create some function that does the cleaning and then tell renamed to apply that function
# across all of the data. Python comes with a handy string function to strip white space called "strip()".
# When we pass this in to rename we pass the function as the mapper parameter, and then indicate whether the
# axis should be columns or index (row labels)
new_df=new_df.rename(mapper=str.strip, axis='columns')
# Let's take a look at results
print(new_df.head())
print()

# We can also use the df.columns attribute by assigning to it a list of column names which will directly
# rename the columns. This will directly modify the original dataframe and is very efficient especially when
# you have a lot of columns and you only want to change a few. This technique is also not affected by subtle
# errors in the column names, a problem that we just encountered. With a list, you can use the list index to
# change a certain value or use list comprehension to change all of the values

# As an example, lets change all of the column names to lower case. First we need to get our list
cols = list(df.columns)
# Then a little list comprehenshion
cols = [x.lower().strip() for x in cols]
# Then we just overwrite what is already in the .columns attribute
df.columns=cols
# And take a look at our results
print(df.head())


"""
This part shows how to load a CSV file into a Pandas DataFrame and clean column names.

Key notes:
- Use pd.read_csv() to load CSV files into a DataFrame.
- By default, Pandas creates a new index starting from 0.
- You can use index_col to set an existing column as the index.
- Column names can be renamed using .rename().
- Extra spaces in column names can break renaming.
- Use str.strip with .rename() to remove hidden spaces safely.
- You can also rename all columns directly using df.columns.
- List comprehension is useful for cleaning column names (lowercase, strip spaces).
- Cleaning column names early prevents many future bugs.
"""
