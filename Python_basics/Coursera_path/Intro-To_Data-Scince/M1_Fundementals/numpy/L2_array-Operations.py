import numpy as np
import math

# We can do many things on arrays, such as mathematical manipulation (addition, subtraction, square,
# exponents) as well as use boolean arrays, which are binary values. We can also do matrix manipulation such
# as product, transpose, inverse, and so forth.

# Arithmetic operators on array apply elementwise.

# Let's create a couple of arrays
a = np.array([10,20,30,40])
b = np.array([1, 2, 3,4])

# Now let's look at a minus b
c = a-b
print(c)
print()
# And let's look at a times b
d = a*b
print(d)
print()


# With arithmetic manipulation, we can convert current data to the way we want it to be. Here's a real-world
# problem I face - I moved down to the United States about 6 years ago from Canada. In Canada we use celcius
# for temperatures, and my wife still hasn't converted to the US system which uses farenheit. With numpy I
# could easily convert a number of farenheit values, say the weather forecase, to ceclius

# Let's create an array of typical Ann Arbor winter farenheit values
farenheit = np.array([0,-10,-5,-15,0])

# And the formula for conversion is ((°F − 32) × 5/9 = °C)
celcius = (farenheit - 31) * (5/9)
print(celcius)
print()

# Great, so now she knows it's a little chilly outside but not so bad.

# Another useful and important manipulation is the boolean array. We can apply an operator on an array, and a
# boolean array will be returned for any element in the original, with True being emitted if it meets the condition and False oetherwise.
# For instance, if we want to get a boolean array to check celcius degrees that are greater than -20 degrees
print(celcius > -20)
print()
# Here's another example, we could use the modulus operator to check numbers in an array to see if they are even.
# Recall that modulus does division but throws away everything but the remainder (decimal) portion)
print(celcius % 2 == 0)
print()

# Besides elementwise manipulation, it is important to know that numpy supports matrix manipulation. Let's
# look at matrix product. if we want to do elementwise product, we use the "*" sign
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A)
print()
print(B)
print()
print(A*B)
print()
# if we want to do matrix product, we use the "@" sign or use the dot function
print(A@B)
print()


# You don't have to worry about complex matrix operations for this course, but it's important to know that
# numpy is the underpinning of scientific computing libraries in python, and that it is capable of doing both
# element-wise operations (the asterix) as well as matrix-level operations (the @ sign). There's more on this
# in a subsequent course.

# A few more linear algebra concepts are worth layering in here. You might recall that the product of two
# matrices is only plausible when the inner dimensions of the two matrices are the same. The dimensions refer
# to the number of elements both horizontally and vertically in the rendered matricies you've seen here. We
# can use numpy to quickly see the shape of a matrix:
print(A.shape)
print()

# When manipulating arrays of different types, the type of the resulting array will correspond to
# the more general of the two types. This is called upcasting.

# Let's create an array of integers
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.dtype)

# Now let's create an array of floats
array2 = np.array([[7.1, 8.2, 9.1], [10.4, 11.2, 12.3]])
print(array2.dtype)
print()

# Integers (int) are whole numbers only, and Floating point numbers (float) can have a whole number portion
# and a decimal portion. The 64 in this example refers to the number of bits that the operating system is
# reserving to represent the number, which determines the size (or precision) of the numbers that can be
# represented.
# Let's do an addition for the two arrays
array3=array1+array2
print(array3)
print(array3.dtype)
print()
# Notice how the items in the resulting array have been upcast into floating point numbers

# Numpy arrays have many interesting aggregation functions on them, such as  sum(), max(), min(), and mean()
print(array3.sum())
print(array3.max())
print(array3.min())
print(f'{array3.mean():.2f}')
print()
# For two dimensional arrays, we can do the same thing for each row or column
# let's create an array with 15 elements, ranging from 1 to 15,
# with a dimension of 3X5
b = np.arange(1,16,1).reshape(3,5)
print(b)