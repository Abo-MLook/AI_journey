import math

#Lambda in Python is a small anonymous function, useful for creating simple,
# one-off functions without formally defining them using def.

#  Syntax:
#  lambda arguments: expression

squared = lambda num : num * num
print(squared(2))

add_two = lambda x : x + 2
print(add_two(4))



z = lambda a,b : math.sqrt(a**2 + b**2)
print(z(3,4))

#==================

