# Let's bring in pandas and numpy as usual
import pandas as pd

# Pandas has four main time related classes. Timestamp, DatetimeIndex, Period, and PeriodIndex. First, let's
# look at Timestamp. It represents a single timestamp and associates values with points in time.

# For example, let's create a timestamp using a string 9/1/2019 10:05AM, and here we have our timestamp.
# Timestamp is interchangeable with Python's datetime in most cases.
print(pd.Timestamp('9/1/2019 10:05AM'))
print()

# We can also create a timestamp by passing multiple parameters such as year, month, date, hour,
# minute, separately
print(pd.Timestamp(2019, 12, 20, 0, 0))
print()


# Timestamp also has some useful attributes, such as isoweekday(), which shows the weekday of the timestamp
# note that 1 represents Monday and 7 represents Sunday
print(pd.Timestamp(2019, 12, 20, 0, 0).isoweekday())
print()


# You can find extract the specific year, month, day, hour, minute, second from a timestamp
print(pd.Timestamp(2019, 12, 20, 5, 2, 23).second)
print()

# Suppose we weren't interested in a specific point in time and instead wanted a span of time. This is where
# the Period class comes into play. Period represents a single time span, such as a specific day or month.

# Here we are creating a period that is January 2016,
print(pd.Period('1/2016'))
print()


# You'll notice when we print that out that the granularity of the period is M for month, since that was the
# finest grained piece we provided. Here's an example of a period that is March 5th, 2016.
print(pd.Period('3/5/2016'))
print()

# Period objects represent the full timespan that you specify. Arithmetic on period is very easy and
# intuitive, for instance, if we want to find out 5 months after January 2016, we simply plus 5
print(pd.Period('1/2016') + 5)
print()

# From the result, you can see we get June 2016. If we want to find out two days before March 5th 2016, we
# simply subtract 2
print(pd.Period('3/5/2016') - 2)
print()


# The key here is that the period object encapsulates the granularity for arithmetic

# The index of a timestamp is DatetimeIndex. Let's look at a quick example. First, let's create our example
# series t1, we'll use the Timestamp of September 1st, 2nd and 3rd of 2016. When we look at the series, each
# Timestamp is the index and has a value associated with it, in this case, a, b and c.

t1 = pd.Series(
    list('abc'),
    [
        pd.Timestamp('2016-09-01'),
        pd.Timestamp('2016-09-02'),
        pd.Timestamp('2016-09-03')
    ]
)

print(t1)
print()

# Looking at the type of our series index, we see that it's DatetimeIndex.
print(type(t1.index))
print()


# Similarly, we can create a period-based index as well.
t2 = pd.Series(
    list('def'),
    [
        pd.Period('2016-09'),
        pd.Period('2016-10'),
        pd.Period('2016-11')
    ]
)

print(t2)
print()


# Looking at the type of the ts2.index, we can see that it's PeriodIndex.
print(type(t2.index))
print()
