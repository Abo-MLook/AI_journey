import numpy as np

#========================== Load data from a file
print("Load data from a file :")
file_data = np.genfromtxt('data.txt',delimiter=',') # the data will be float as defualt
file_data = file_data.astype(int)  # cast it into integer
print(file_data)
print()
#----- exit


#========================== Load data from a file
#print("Load data from a file :")

#----- exit

#========================== Boolean Masking and Advances Indexing
print("Boolean Masking and Advances Indexing :")
print("print boolean")
print(file_data>50)
print("print values")
print(file_data[file_data > 50]) #  you can add more conditions

#----- exit