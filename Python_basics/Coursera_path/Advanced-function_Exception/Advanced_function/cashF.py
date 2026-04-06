import functools

@functools.cache  # try to print without this
def factorial(n):
    print(f"Calculating {n}!")
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(6))
