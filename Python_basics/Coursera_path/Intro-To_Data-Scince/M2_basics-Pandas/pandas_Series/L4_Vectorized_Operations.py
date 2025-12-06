import pandas as pd

# Now we know how to get data out of the series, let's talk about working with the data. A common
# task is to want to consider all of the values inside of a series and do some sort of
# operation. This could be trying to find a certain number, or summarizing data or transforming
# the data in some way.
# A typical programmatic approach to this would be to iterate over all the items in the series,
# and invoke the operation one is interested in. For instance, we could create a Series of
# integers representing student grades, and just try and get an average grade

grades = pd.Series([90, 80, 70, 60])
total = 0
for grade in grades:
    total+=grade
print(total/len(grades))
# This works, but it's slow. Modern computers can do many tasks simultaneously, especially,
# but not only, tasks involving mathematics.

# Pandas and the underlying numpy libraries support a method of computation called vectorization.
# Vectorization works with most of the functions in the numpy library, including the sum function.

# Here's how we would really write the code using the numpy sum method. First we need to import
# the numpy module

import numpy as np

# Then we just call np.sum and pass in an iterable item. In this case, our panda series.

total = np.sum(grades)
print(total/len(grades))
print()


# Now both of these methods create the same value, but is one actually faster? The Jupyter
# Notebook has a magic function which can help.

# First, let's create a big series of random numbers. This is used a lot when demonstrating
# techniques with Pandas
numbers = pd.Series(np.random.randint(0,1000,10000))

# Now lets look at the top five items in that series to make sure they actually seem random. We
# can do this with the head() function
print(numbers.head())
print(len(numbers))
print()


# Let's run timeit with our original iterative code. You can give timeit the number of loops that
# you would like to run. By default, it is 1,000 loops. I'll ask timeit here to use 100 runs because
# we're recording this

import timeit

def loop_mean():
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def pybuiltin():
    total = sum(numbers)
    return total / len(numbers)

def numpy_mean():
    total = np.sum(numbers)
    return total / len(numbers)

# Run each 100 times (like -n 100)
loop_time = timeit.timeit(loop_mean, number=100)
numpy_time = timeit.timeit(numpy_mean, number=100)
pybul_time = timeit.timeit(pybuiltin, number=100)

print("Loop version:", loop_time)
print("Python built in version:", pybul_time)
print("NumPy version:", numpy_time)
print()
print()
# Wow! This is a pretty shocking difference in the speed and demonstrates why one should be
# aware of parallel computing features and start thinking in functional programming terms.
# Put more simply, vectorization is the ability for a computer to execute multiple instructions
# at once, and with high performance chips, especially graphics cards, you can get dramatic
# speedups. Modern graphics cards can run thousands of instructions in parallel.



# A Related feature in pandas and nummy is called broadcasting. With broadcasting, you can
# apply an operation to every value in the series, changing the series. For instance, if we
# wanted to increase every random variable by 2, we could do so quickly using the += operator
# directly on the Series object.

# Let's look at the head of our series
print(numbers.head())
print()

numbers += 2
print(numbers.head())
print()

# The procedural way of doing this would be to iterate through all of the items in the
# series and increase the values directly. Pandas does support iterating through a series
# much like a dictionary, allowing you to unpack values easily.

# We can use the iteritems() function which returns a label and value
for label , value in numbers.items():
    # in the early version of pandas we would use the set_value() function
    # in the current version, we use the iat() or at() functions,
    numbers.at[label] = value + 2

print(numbers.head())

# Lets take a look at some speed comparisons.



# First, lets try five loops using the iterative approach
numbers = pd.Series(np.random.randint(0,1000,1000))
def iterative():
    global numbers
    for label , val in numbers.items():
        numbers.at[label] = val+2
    return numbers

itert_time = timeit.timeit(iterative,number=100)


# Now lets try that using the broadcasting methods
numbers = pd.Series(np.random.randint(0,1000,1000))
def broadcasting():
    global numbers
    numbers +=2
    return numbers

broad_time = timeit.timeit(broadcasting,number=100)

print()
print(f"iterative approach time :  {itert_time}")
print(f"broadcasting methods time :  {broad_time}")
# Amazing. Not only is it significantly faster, but it's more concise and even easier
# to read too. The typical mathematical operations you would expect are vectorized, and the
# nump documentation outlines what it takes to create vectorized functions of your own.


"""
This part compares slow looping vs fast vectorized operations in Pandas and NumPy.

Key notes:
- You can loop through a Series to do calculations, but it is slow.
- Using built-in functions like sum() is faster than manual loops.
- Using NumPy functions like np.sum() is MUCH faster than both.
- timeit is used to measure and compare execution speed.
- Vectorization means performing operations on all values at once instead of one-by-one.
- Broadcasting applies an operation to the entire Series instantly (like numbers += 2).
- Broadcasting is significantly faster and cleaner than using loops.
- Always prefer:
  → NumPy functions for calculations
  → Broadcasting for transforming data
  → Avoid manual loops unless absolutely necessary
"""
