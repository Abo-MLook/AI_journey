# To load a dataset in Numpy, we can use the genfromtxt() function. We can specify data file name, delimiter
# (which is optional but often used), and number of rows to skip if we have a header row, hence it is 1 here

# The genfromtxt() function has a parameter called dtype for specifying data types of each column this
# parameter is optional. Without specifying the types, all types will be casted the same to the more
# general/precise type

#wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header=1)
#wines

# So all rows combined but only the first column from them would be
#print("one integer 0 for slicing: ", wines[:, 0])
# But if we wanted the same values but wanted to preserve that they sit in their own rows we would write
#print("0 to 1 for slicing: \n", wines[:, 0:1])