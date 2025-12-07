# Let's look at an example. First, we'll bring in our pandas and numpy libraries
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
import numpy as np

# Let's look at some US census data
df = pd.read_csv('census.csv')
# And exclude state level summarizations, which have sum level value of 40
df = df[df['SUMLEV']==50]
print(df.head())
print()
print(df.groupby('STNAME').head())

for group, frame in df.groupby('STNAME'):
    # You'll notice there are two values we set here. groupby() returns a tuple, where the first value is the
    # value of the key we were trying to group by, in this case a specific state name, and the second one is
    # projected dataframe that was found for that group
    # Now we include our logic in the "apply" step, which is to calculate an average of the census2010pop
    avg = np.average(frame['CENSUS2010POP'])
    # And print the results
    print('Counties in state ' + group +
          ' have an average population of ' + str(avg))
print()

# And we don't have to worry about the combine step in this case, because all of our data transformation is
# actually printing out results.
# Wow, what a huge difference in speed. An improve by roughly by two factors!

# Now, 99% of the time, you'll use group by on one or more columns. But you can also provide a function to
# group by and use that to segment your data.

# This is a bit of a fabricated example but lets say that you have a big batch job with lots of processing and
# you want to work on only a third or so of the states at a given time. We could create some function which
# returns a number between zero and two based on the first character of the state name. Then we can tell group
# by to use this function to split up our data frame. It's important to note that in order to do this you need
# to set the index of the data frame to be the column that you want to group by first.

# We'll create some new function called set_batch_number and if the first letter of the parameter is a capital
# M we'll return a 0. If it's a capital Q we'll return a 1 and otherwise we'll return a 2. Then we'll pass
# this function to the data frame

df = df.set_index('STNAME')

def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

# The dataframe is supposed to be grouped by according to the batch number And we will loop through each batch
# group
for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
print()

# Let's take one more look at an example of how we might group data. In this example, I want to use a dataset
# of housing from airbnb. In this dataset there are two columns of interest, one is the cancellation_policy
# and the other is the review_scores_value.
df=pd.read_csv("listings.csv")
df.head()
print()

# So, how would I group by both of these columns? A first approach might be to promote them to a multiindex
# and just call groupby()
df=df.set_index(["cancellation_policy","review_scores_value"])

# When we have a multiindex we need to pass in the levels we are interested in grouping by
for group, frame in df.groupby(level=(0,1)):
    print(group)
print()

# This seems to work ok. But what if we wanted to group by the cancelation policy and review scores, but
# separate out all the 10's from those under ten? In this case, we could use a function to manage the
# groupings

def grouping_fun(item):
    # Check the "review_scores_value" portion of the index. item is in the format of
    # (cancellation_policy,review_scores_value
    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],"not 10.0")

for group, frame in df.groupby(by=grouping_fun):
    print(group)

print()
print(df.head())