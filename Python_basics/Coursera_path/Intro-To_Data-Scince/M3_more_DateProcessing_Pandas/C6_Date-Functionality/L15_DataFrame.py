import pandas as pd
import numpy as np


# Next, let's look at a few tricks for working with dates in a DataFrame. Suppose we want to look at nine
# measurements, taken bi-weekly, every Sunday, starting in October 2016. Using date_range, we can create this
# DatetimeIndex. In date_range, we have to either specify the start or end date. If it is not explicitly
# specified, by default, the date is considered the start date. Then we have to specify number of periods, and
# a frequency. Here, we set it to "2W-SUN", which means biweekly on Sunday

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)
print()


# There are many other frequencies that you can specify. For example, you can do business day
print(pd.date_range('10-01-2016', periods=9, freq='B'))
print()


# Or you can do quarterly, with the quarter start in June
print(pd.date_range('04-01-2016', periods=12, freq='QS-JUN'))
print()

# Now, let's go back to our weekly on Sunday example and create a DataFrame using these dates, and some random
# data, and see what we can do with it.

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame(
    {
        'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
        'Count 2': 120 + np.random.randint(-5, 10, 9)
    },
    index=dates
)
print(df)
print()


# First, we can check what day of the week a specific date is. For example, here we can see that all the dates
# in our index are on a Sunday. Which matches the frequency that we set
print(df.index.weekday)
print()

print(df.index.weekday)
print()

print(df.index.weekday)
print()

# Suppose we want to know what the mean count is for each month in our DataFrame. We can do this using
# resample. Converting from a higher frequency from a lower frequency is called downsampling
print(df.resample('ME').mean())
print()


# Now let's talk about datetime indexing and slicing, which is a wonderful feature of the pandas DataFrame.
# For instance, we can use partial string indexing to find values from a particular year,
print(df.loc['2017'])
print()

# Or we can do it from a particular month
print(df.loc['2016-12'])
print()


# Or we can even slice on a range of dates For example, here we only want the values from December 2016
# onwards.
print(df.loc['2016-12':])
print()


print(df.loc['2016'])
print()
