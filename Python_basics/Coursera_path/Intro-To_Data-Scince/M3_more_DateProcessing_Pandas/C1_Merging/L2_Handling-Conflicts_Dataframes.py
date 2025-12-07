import pandas as pd
# So what happens when we have conflicts between the DataFrames? Let's take a look by creating new staff and
# student DataFrames that have a location information added to them.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR',
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion',
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader',
                          'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business',
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law',
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering',
                            'Location': '512 Wilson Crescent'}])

# In the staff DataFrame, this is an office location where we can find the staff person. And we can see the
# Director of HR is on State Street, while the two students are on Washington Avenue, and these locations just
# happen to be right outside my window as I film this. But for the student DataFrame, the location information
# is actually their home address.

# The merge function preserves this information, but appends an _x or _y to help differentiate between which
# index went with which column of data. The _x is always the left DataFrame information, and the _y is always
# the right DataFrame information.

# Here, if we want all the staff information regardless of whether they were students or not. But if they were
# students, we would want to get their student details as well.Then we can do a left join and on the column of
# Name

print(pd.merge(staff_df, student_df, how='left', on='Name'))
print("")
# From the output, we can see there are columns Location_x and Location_y. Location_x refers to the Location
# column in the left dataframe, which is staff dataframe and Location_y refers to the Location column in the
# right dataframe, which is student dataframe.

# Before we leave merging of DataFrames, let's talk about multi-indexing and multiple columns. It's quite
# possible that the first name for students and staff might overlap, but the last name might not. In this
# case, we use a list of the multiple columns that should be used to join keys from both dataframes on the on
# parameter. Recall that the column name(s) assigned to the on parameter needs to exist in both dataframes.

# Here's an example with some new student and staff data
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins',
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks',
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde',
                          'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond',
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith',
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks',
                            'School': 'Engineering'}])

# As you see here, James Wilde and James Hammond don't match on both keys since they have different last
# names. So we would expect that an inner join doesn't include these individuals in the output, and only Sally
# Brooks will be retained.
print(pd.merge(staff_df, student_df, how='inner', on=['First Name','Last Name']))
print()
# Joining dataframes through merging is incredibly common, and you'll need to know how to pull data from
# different sources, clean it, and join it for analysis. This is a staple not only of pandas, but of database
# technologies as well.