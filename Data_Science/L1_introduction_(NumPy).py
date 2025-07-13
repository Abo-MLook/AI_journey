import numpy as np

# NumPy is a Python library for efficient handling of large, multi-dimensional arrays and matrices, with high-level
# mathematical functions for operations. It’s essential for data science, machine learning, and scientific computing.




#========================== initialize

ob1 = np.array([1,2,3])
print(ob1)

# Two Dimensional array
print("\n# Two dimantional array:")
ob_2d = np.array([[1,2,3],[4,5,6]])
print(ob_2d)


#========================== Dimension

# getting the Dimensions       using      .ndim
print(f"\nob1 is {ob1.ndim}D array \nob_2d is {ob_2d.ndim}D array")

#========================== Shapes

# getting the shapes       using      .shape
print(f"\nob1 is {ob1.shape} matrice \nob_2d is {ob_2d.shape} matrice")
print()

#========================== dtype

# getting the type       using      .dtype
print(f"ob1 is {ob1.dtype}") # int64 is to much for low numbers

ob1 = ob1.astype(np.int16)
print(f"ob1 is {ob1.dtype}") # changed

# or you can from creating put it
ob2 = np.array([1,2,3],"int32")
print(f"ob2 is {ob2.dtype}")
print()

#========================== Sizes and types
# .itemsize size of item in byte
# .size  the number of items
print(f"ob1 :each elemnt has byte of {ob1.itemsize} and total elements are {ob1.size} , Total bytes as whole is {ob1.itemsize * ob1.size}")

print(f"ob2 :each elemnt has byte of {ob2.itemsize} and total elements are {ob2.size} , Total bytes as whole is {ob2.nbytes}")



