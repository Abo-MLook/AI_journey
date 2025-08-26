# What is a Higher-Order Function?
# A higher-order function is any function that:
# 1- Takes another function as an argument, OR
# 2- Returns a function as a result.

# Why is This Useful?
# ➡️ Code reusability: Write functions that work with other functions.
# ➡️ Simplifies complex logic: You can compose small functions into bigger logic.
# ➡️ Functional programming style: Makes your code more declarative and clean.

def Funcbuilder(x):
    return lambda num : num + x

var1 = Funcbuilder(10) # now 10 will be the x value, the lamda returning can be call now and passed then returned final value
var2= Funcbuilder(20)

print(var1(3)) # calling;  num = 3, x = 10 from before;  return 3 + 10
print(var2(5))
#--------------------------------------------------------------------------

numbers = [1,4,2,3,7,8]
print(f"numbers are : {numbers}\n")
#-------------------------------------------------------------------------

# map()	  ;       map(func, iterable)	   ;Apply a function to each element

sequerd_numbers = list(map(lambda x : x * x , numbers))

print(f"using (map) with lambda, sequered are  : {sequerd_numbers}")

#===============================

# filter()	      filter(func, iterable)	       Keep items where function is (True)

#odd_numbers = list(filter(lambda x : x % 2 !=0,numbers))    work ✅
# or
is_odd = lambda x: x % 2 != 0
odd_numbers = list(filter(is_odd,numbers))

print(f"using (filter) with lambda, odds are  : {odd_numbers}")
#===============================

# reduce() 	reduce(func, iterable)	Combine elements into one result
from functools import reduce

total = reduce(lambda x , current : x + current,numbers)

print(f"using (reduce) with lambda, total are  : {total}")

# note reduce can be use for complicit example , for total you can use (sum)
print(f"using sum built in function : {sum(numbers)}")

#-:-:
names = ["Mrwan Alayed","Salah Aladeeme","Bassam Albleehi"]
counting_letters = reduce(lambda x , current : x + len(current),names, 0 ) # because it is string we must add 0 at starting

print(f"using (reduce) with lambda, total letters are   : {counting_letters}")

#=======================================================
# sorted()	  Sort based on a function of each item   	key=lambda x: len(x)

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key = lambda word: len(word))

print(f"using (sorted) with lambda, sorted words are   : {sorted_words}")

#==============================================================
