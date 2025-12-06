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

def numpy_mean():
    total = np.sum(numbers)
    return total / len(numbers)
def pybuiltin():
    total = sum(numbers)
    return total / len(numbers)
# Run each 100 times (like -n 100)
loop_time = timeit.timeit(loop_mean, number=100)
numpy_time = timeit.timeit(numpy_mean, number=100)
pybul_time = timeit.timeit(pybuiltin, number=100)

print("Loop version:", loop_time)
print("Python built in version:", pybul_time)
print("NumPy version:", numpy_time)
