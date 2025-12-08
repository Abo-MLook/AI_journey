import pandas as pd
import numpy as np



# Now, let's look into how to convert to Datetime. Suppose we have a list of dates as strings and we want to
# create a new dataframe

# I'm going to try a bunch of different date formats
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']

# And just some random data
ts3 = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1,
                   columns=list('ab'))

print(ts3)
print()



# Using pandas to_datetime, pandas will try to convert these to Datetime and put them in a standard format.

ts3.index = pd.to_datetime(ts3.index, format='mixed')

print(ts3)
print()



# to_datetime also() has options to change the date parse order. For example, we
# can pass in the argument dayfirst = True to parse the date in European date.

print(pd.to_datetime('4.7.12', dayfirst=True))
print()



# Timedelta ================================

# Timedeltas are differences in times. This is not the same as a a period, but conceptually similar. For
# instance, if we want to take the difference between September 3rd and  September 1st, we get a Timedelta of
# two days.

print(pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016'))
print()

# We can also do something like find what the date and time is for 12 days and three hours past September 2nd,
# at 8:10 AM.

print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))
print()



# Offset =====================================

# Offset is similar to timedelta, but it follows specific calendar duration rules. Offset allows flexibility
# in terms of types of time intervals. Besides hour, day, week, month, etc it also has business day, end of
# month, semi month begin etc

# Let's create a timestamp, and see what day is that

print(pd.Timestamp('9/4/2016').weekday())
print()

# Now we can now add the timestamp with a week ahead

print(pd.Timestamp('9/4/2016') + pd.offsets.Week())
print()

# Now let's try to do the month end, then we would have the last day of Septemer

print(pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd())
print()
