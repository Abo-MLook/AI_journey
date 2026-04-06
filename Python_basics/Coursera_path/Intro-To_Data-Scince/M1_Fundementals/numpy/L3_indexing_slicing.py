import numpy as np

# First we are going to look at integer indexing. A one-dimensional array, works in similar ways as a list -
# To get an element in a one-dimensional array, we simply use the offset index.
a = np.array([1,3,5,7])
print(a[2])
print()
a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
print()
print(a[1])
print()
print(a[1][1])
print()

# if we want to get multiple elements
# for example, 1, 4, and 6 and put them into a one-dimensional array
# we can enter the indices directly into an array function
print(np.array([a[0, 0], a[1, 1], a[2, 1]]))
print()
print()
# we can also do that by using another form of array indexing, which essentiall "zips" the first list and the
# second list up
print(a[[0, 1, 2], [0, 1, 1]])
print()


## Boolean Indexing

# Boolean indexing allows us to select arbitrary elements based on conditions. For example, in the matrix we
# just talked about we want to find elements that are greater than 5 so we set up a conditon a >5
print(a >5)
print()
# This returns a boolean array showing that if the value at the corresponding index is greater than 5
# We can then place this array of booleans like a mask over the original array to return a one-dimensional
# array relating to the true values.
print(a[a>5])
print()
# As we will see, this functionality is essential in the pandas toolkit which is the bulk of this course

## Slicing
# Slicing is a way to create a sub-array based on the original array. For one-dimensional arrays, slicing
# works in similar ways to a list. To slice, we use the : sign. For instance, if we put :3 in the indexing
# brackets, we get elements from index 0 to index 3 (excluding index 3)
a = np.array([0,1,2,3,4,5])
print(a[:3])
print()
# By putting 2:4 in the bracket, we get elements from index 2 to index 4 (excluding index 4)
print(a[2:4])
print()

# For multi-dimensional arrays, it works similarly, lets see an example
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print()
# First, if we put one argument in the array, for example a[:2] then we would get all the elements from the
# first (0th) and second row (1th)
print(a[:2])
print()
# If we add another argument to the array, for example a[:2, 1:3], we get the first two rows but then the
# second and third column values only
print(a[:2, 1:3])
print()

# So, in multidimensional arrays, the first argument is for selecting rows, and the second argument is for
# selecting columns


# It is important to realize that a slice of an array is a view into the same data. This is called passing by
# reference. So modifying the sub array will consequently modify the original array

# Here I'll change the element at position [0, 0], which is 2, to 50, then we can see that the value in the
# original array is changed to 50 as well
print()
import copy
sub_array =  a[:2, 1:3]
# you can solve it using sub_array = copy.deepcopy(a[:2, 1:3]) 
print("sub array index [0,0] value before change:", sub_array[0,0])
sub_array[0,0] = 50
print("sub array index [0,0] value after change:", sub_array[0,0])
print("original array index [0,1] value after change:", a[0,1])


"""
This code demonstrates three essential NumPy indexing techniques—integer indexing, 
boolean indexing, and slicing—along with an important concept about array views.

Integer Indexing:
- Single index for 1D arrays works like lists.
- For 2D arrays, `a[row]` returns a row; `a[row][col]` or `a[row, col]` returns a scalar.
- You can extract multiple arbitrary elements using:
      np.array([a[0,0], a[1,1], a[2,1]])
  or the vectorized form:
      a[[0,1,2], [0,1,1]]

Boolean Indexing:
- Conditions like `a > 5` produce a boolean mask.
- Applying the mask selects only elements where the condition is True:
      a[a > 5]
- This feature becomes even more powerful when working with pandas.

Slicing:
- Works similarly to Python lists for 1D arrays:
      a[:3], a[2:4]
- For 2D arrays:
      a[:2]        → first two rows
      a[:2, 1:3]   → rows 0–1, columns 1–2
- First index slice = rows, second = columns.

Views vs Copies:
- Slices are *views* into the original array, not copies.
- Modifying a slice modifies the original:
      sub = a[:2, 1:3]
      sub[0,0] = 50   → original array changes too
- Use `copy.deepcopy()` or `a[:2, 1:3].copy()` if you need an independent subarray.

Summary:
NumPy indexing provides powerful and efficient ways to access, filter, and reshape data, 
but it’s crucial to remember when operations produce views that share memory with the 
original array.
"""
