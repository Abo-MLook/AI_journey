"""
Input: The performance decorator accepts a single function as its argument.
Wrapped Function: The performance decorator should return a modified ("wrapped") version of the input function that:
Records the start time before running the wrapped function
Executes the wrapped function and stores its resturn value
Records the end time after running the wrapped function
Calculates the elapsed time (end time - start time)
Return Value: The wrapped function should return a tuple with:
The elapsed time (in seconds) taken to execute the wrapped function
The wrapped function's return value
"""

import time

start_time = time.perf_counter()     # "Start" timer
time.sleep(1)                        # Wait one second
end_time = time.perf_counter()       # "Stop" timer
elapsed_time = end_time - start_time # should be *slightly* more than 1

print(elapsed_time) # 1.0045422080000037 (approximately)
#Define a decorator named performance that wraps a function to
# return a tuple with (1) the original return value of the function and (2) the amount of time that it took.
# For example, we should be able to write:

@performance
def add(a, b):
    return a + b

sum_result, time_taken = add(1, 2) # sum_result == 3, time_taken ~= 0
#Hint: to create a decorator named fake_performance that returns a tuple with
# the function call result and a string, we could do the following:

import functools

def fake_performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result, "PUT THE ELAPSED TIME HERE AS A NUMBER"
    return wrapper



# answer :
import functools
import time

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start timer
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()  # Stop timer
        elapsed_time = end_time - start_time  # Calculate elapsed time
        return result, elapsed_time  # Return function result and elapsed time
    return wrapper

# Example usage
@performance
def add(a, b):
    return a + b

# Call the decorated function
sum_result, time_taken = add(1, 2)
print("Sum Result:", sum_result)  # Should print: Sum Result: 3
print("Time Taken:", time_taken)  # Should print the time taken to execute
