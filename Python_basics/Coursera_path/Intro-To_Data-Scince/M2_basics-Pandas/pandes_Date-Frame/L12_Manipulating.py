# Let's start by bringing in pandas
import pandas as pd
from markdown_it.rules_inline.backticks import regex

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# And load our dataset. We're going to be cleaning the list of presidents in the US from wikipedia
df=pd.read_csv("presidents.csv")
# And lets just take a look at some of the data
print(df.head())
print()
# Ok, we have some presidents, some dates, I see a bunch of footnotes in the "Born" column which might cause
# issues. Let's start with cleaning up that name into firstname and lastname. I'm going to tackle this with
# a regex. So I want to create two new columns and apply a regex to the projection of the "President" column.

# Here's one solution, we could make a copy of the President column
df["First"]=df['President']
# Then we can call replace() and just have a pattern that matches the last name and set it to an empty string
df["First"]=df["First"].replace("[ ].*", "", regex=True)
# Now let's take a look
print(df.head())
print()

# That works, but it's kind of gross. And it's slow, since we had to make a full copy of a column then go
# through and update strings. There are a few other ways we can deal with this. Let me show you the most
# general one first, and that's called the apply() function. Let's drop the column we made first
del(df["First"])

# The apply() function on a dataframe will take some arbitrary function you have written and apply it to
# either a Series (a single column) or DataFrame across all rows or columns. Lets write a function which
# just splits a string into two pieces using a single row of data
def splitname(row):
    # The row is a single Series object which is a single row indexed by column values
    # Let's extract the firstname and create a new entry in the series
    row['First']=row['President'].split(" ")[0]
    # Let's do the same with the last word in the string
    row['Last']=row['President'].split(" ")[-1]
    # Now we just return the row and the pandas .apply() will take of merging them back into a DataFrame
    return row

# Now if we apply this to the dataframe indicating we want to apply it across columns
df=df.apply(splitname, axis='columns')
print(df.head())
print()

# Pretty questionable as to whether that is less gross, but it achieves the result and I find that I use the
# apply() function regularly in my work. The pandas series has a couple of other nice convenience functions
# though, and the next I would like to touch on is called .extract(). Lets drop our firstname and lastname.
del(df['First'])
del(df['Last'])

# Extract takes a regular expression as input and specifically requires you to set capture groups that
# correspond to the output columns you are interested in. And, this is a great place for you to pause the
# video and reflect - if you were going to write a regular expression that returned groups and just had the
# firstname and lastname in it, what would that look like?

# Here's my solution, where we match three groups but only return two, the first and the last name
pattern="(^[\w]*)(?:.* )([\w]*$)"

# Now the extract function is built into the str attribute of the Series object, so we can call it
# using Series.str.extract(pattern)
print(df["President"].str.extract(pattern).head())
print()

# So that looks pretty nice, other than the column names. But if we name the groups we get named columns out
pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

# Now call extract
names=df["President"].str.extract(pattern).head()
print(names)
print()


# Now lets move on to clean up that Born column. First, let's get rid of anything that isn't in the
# pattern of Month Day and Year.
df["Born"]=df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
print(df["Born"].head())
print()

# So, that cleans up the date format. But I'm going to foreshadow something else here - the type of this
# column is object, and we know that's what pandas uses when it is dealing with string. But pandas actually
# has really interesting date/time features - in fact, that's one of the reasons Wes McKinney put his efforts
# into the library, to deal with financial transactions. So if I were building this out, I would actually
# update this column to the write data type as well
df["Born"]=pd.to_datetime(df["Born"])
print(df["Born"].head())
print()
print(df.head())
print()
print(df["Age"] .head())
df["Age"] = df["Age"].replace(" .*","",regex =True)
print()
print(df["Age"] .head())

print()
print(df.columns)
print(df.head())

"""
This code focuses on cleaning a dataset of US presidents. Key points:

1. **Cleaning President Names**:
   - We split the "President" column into first and last names. 
   - **Regex Method**: We used a regular expression to remove the last name from the full name for the first name.
   - **Apply Function**: A more general solution uses the `apply()` function to split the "President" column into two new columns: 'First' and 'Last'.
   - **Extract Method**: For better performance and readability, we use the `.str.extract()` method with a regex pattern to extract the first and last names as separate columns, naming them `First` and `Last`.

2. **Cleaning Birth Date**:
   - The "Born" column contains date information in inconsistent formats.
   - We used `.str.extract()` with a regex pattern to capture the "Month Day, Year" format.
   - **Converting to Datetime**: After cleaning the date format, we convert the column to a proper datetime data type using `pd.to_datetime()`.

3. **Cleaning Age Column**:
   - We used a regex pattern to remove unwanted characters from the "Age" column.

4. **General Notes**:
   - **Regex**: Regular expressions are used to match patterns in strings, which makes them useful for cleaning data like names, dates, and ages.
   - **Pandas Methods**: Functions like `.apply()`, `.extract()`, and `str` methods (e.g., `str.extract()`) help clean and transform columns effectively.
   - **Data Types**: After cleaning the "Born" column, it's converted to the correct datetime format to ensure proper handling in further analysis.

This code demonstrates essential techniques for text and date cleaning in pandas, making the data ready for further analysis.
"""
