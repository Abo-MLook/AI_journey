# Missing values appear as None or NaN in pandas
# Very common during data cleaning
# Missing data can happen for many reasons
# Example: survey questions left unanswered
# If missing data relates to other variables → Missing at Random (MAR)
# Example: follow-up interest correlated with gender or ethnicity
# If missing data has no relation to any variable → Missing Completely at Random (MCAR)
# Some data is missing because it was never collected
# Or because it logically doesn't apply
# Common case: merging datasets from different sources
# Example: students listed with offices (most students have no offices)
# pandas provides multiple ways to handle missing data

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Pandas is pretty good at detecting missing values directly from underlying data formats, like CSV files.
# Although most missing valuse are often formatted as NaN, NULL, None, or N/A, sometimes missing values are
# not labeled so clearly. For example, I've worked with social scientists who regularly used the value of 99
# in binary categories to indicate a missing value. The pandas read_csv() function has a parameter called
# na_values to let us specify the form of missing values. It allows scalar, string, list, or dictionaries to
# be used.

# Let's load a piece of data from a file called log.csv
df = pd.read_csv('class_grades.csv')
print(df.head(10))
print()
# We can actually use the function .isnull() to create a boolean mask of the whole dataframe. This effectively
# broadcasts the isnull() function to every cell of data.
mask=df.isnull()
print(mask.head(10))
print()
# This can be useful for processing rows based on certain columns of data. Another useful operation is to be
# able to drop all of those rows which have any missing data, which can be done with the dropna() function.
print(df.dropna().head(10))
print()
# Note how the rows indexed with 2, 3, 7, and 11 are now gone. One of the handy functions that Pandas has for
# working with missing values is the filling function, fillna(). This function takes a number or parameters.
# You could pass in a single value which is called a scalar value to change all of the missing data to one
# value. This isn't really applicable in this case, but it's a pretty common use case.

# So, if we wanted to fill all missing values with 0, we would use fillna
df.fillna(0, inplace=True)
print(df.head(10))
print()
# Note that the inplace attribute causes pandas to fill the values inline and does not return a copy of the
# dataframe, but instead modifies the dataframe you have.


"""
This code demonstrates how to handle missing data in pandas, which is common during data cleaning. Key points:

- **Types of Missing Data**:
  - **Missing at Random (MAR)**: Missing data is related to other variables (e.g., gender or ethnicity).
  - **Missing Completely at Random (MCAR)**: Missing data has no relationship with other variables.
  - Missing data can occur due to various reasons, such as non-response in surveys or data not collected.

- **Identifying Missing Data**:
  - Missing values in pandas are represented as `None` or `NaN`.
  - Use `.isnull()` to create a boolean mask indicating missing values in the DataFrame.

- **Handling Missing Data**:
  - **Dropping Rows with Missing Data**:
    - `df.dropna()` removes any rows that have missing values.
    - Example: Dropping rows with missing data results in a smaller DataFrame without the rows that had missing values.

  - **Filling Missing Data**:
    - `df.fillna(value)` can replace missing data with a specified value, such as `0` in this example.
    - `inplace=True` modifies the original DataFrame rather than returning a new one.

- **Custom Missing Value Representations**:
  - Sometimes missing data isn't explicitly marked as `NaN`. For example, `99` might be used to represent missing data in some datasets.
  - The `na_values` parameter in `read_csv()` allows you to specify custom missing value representations.

These techniques help you clean datasets by identifying, removing, or filling missing values, ensuring your data is ready for analysis.
"""
