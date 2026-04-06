# Importing necessary modules for date/time operations
import datetime as dt
import time as tm

# Getting the current time in seconds since the Unix epoch (January 1, 1970)
tm.time()  # Outputs a floating point number representing the time in seconds
# Example output: 1476714510.468699

# Converting the timestamp to a datetime object
dtnow = dt.datetime.fromtimestamp(tm.time())  # Creates a datetime object from the timestamp
# Example output: datetime.datetime(2016, 10, 17, 10, 28, 40, 500572)
print(dtnow)
# Extracting different components (year, month, day, hour, minute, second) from the datetime object
#dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
# Output: (2016, 10, 17, 10, 28, 40)
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour)
# Creating a timedelta object that represents a duration of 100 days
delta = dt.timedelta(days=100)  # 100 days duration
# Example output: datetime.timedelta(100)

# Getting the current date without the time part (just the year, month, and day)
today = dt.date.today()  # Returns the current local date
# Example output: datetime.date(2025, 12, 5)
print(today)
# Subtracting 100 days from today's date
print(today - delta ) # This will give a date that is 100 days before today's date
# Example output: datetime.date(2025, 8, 26)

# Checking if today's date is greater than the date after subtracting 100 days
print(today > today - delta ) # This will return a boolean (True or False)
# Output: True, as today's date is indeed later than the date 100 days ago
