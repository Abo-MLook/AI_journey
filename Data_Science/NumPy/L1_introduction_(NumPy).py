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

# getting the shapes       using      .shape       like ob_2d  is  2 x 3
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
print()


#========================== Accessing and Changing elements
#--Accessing :
print("Accessing:")
ob3 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(ob3)
print(f"{ob3[0,1]}")
print(f"first row : {ob3[0,:]}")
print(f"theird column : {ob3[:,2]}") # like list and so on ... [start : stop : step] can be used

print(f"row from 2 to 6 : {ob3[0,1:-1:1]}")
# The first 0 refers to the first row.
# The second part 1:-1:1 is slicing the columns. so on...

#--Changing :
print("Changing:")
ob3[0,0] = 7
print(ob3)
ob3[:,2] = [10,3]
print(ob3)
print()
#========================== Accessing and Changing elements for 3D array
ob_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(ob_3d)
print(f"{ob_3d[0,1,1]}") # index is out to in
print(f"{ob_3d[0,:]}")
print()
print(f"{ob_3d[:,:,0]}") # and so on ...

print()
ob_3d[1,:,:] = [[1,4],[9,16]]
print(ob_3d)



# 🔗 Indexing: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.indexing.html