# What is a Higher-Order Function?
# A higher-order function is any function that:
# 1- Takes another function as an argument, OR
# 2- Returns a function as a result.

# Why is This Useful?
# ➡️ Code reusability: Write functions that work with other functions.
# ➡️ Simplifies complex logic: You can compose small functions into bigger logic.
# ➡️ Functional programming style: Makes your code more declarative and clean.

from functools import reduce


def Funcbuilder(x):
    return lambda num: num + x


# now 10 will be the x value, the lamda returning can be call now and passed then returned final value
var1 = Funcbuilder(10)
var2 = Funcbuilder(20)

print(var1(3))  # calling;  num = 3, x = 10 from before;  return 3 + 10
print(var2(5))
# --------------------------------------------------------------------------

numbers = [1, 4, 2, 3, 7, 8]
print(f"numbers are : {numbers}\n")
# -------------------------------------------------------------------------


def squer(x):
    return x * x


# map()	  ;       map(func, iterable)	   ;Apply a function to each element


sequerd_numbers = list(map(lambda x: x * x, numbers))
sequerd_numbers1 = list(map(squer, numbers))


print(f"using (map) with lambda, sequered are  : {sequerd_numbers}")
print(f"using (map) with function, sequered are  : {sequerd_numbers1}")

# ===============================

# filter()	      filter(func, iterable)	       Keep items where function is (True)

# odd_numbers = list(filter(lambda x : x % 2 !=0,numbers))    work ✅
# or


def is_odd(x): return x % 2 != 0


# odd_numbers = list(filter(lambda x : x % 2 !=0,numbers))
odd_numbers = list(filter(is_odd, numbers))

print(f"using (filter) with lambda, odds are  : {odd_numbers}")
# ===============================

# reduce() 	reduce(func, iterable)	Combine elements into one result

total = reduce(lambda x, current: x + current,
               numbers, 1)  # make it start at 1

print(f"using (reduce) with lambda, total are  : {total}")

# note reduce can be use for complicit example , for total you can use (sum)
print(f"using sum built in function : {sum(numbers)}")

# -:-:
names = ["Mrwan Alayed", "Salah Aladeeme", "Bassam Albleehi"]
# because it is string we must add 0 at starting
counting_letters = reduce(lambda x, current: x + len(current), names, 0)

print(f"using (reduce) with lambda, total letters are   : {counting_letters}")

# =======================================================
# sorted()	  Sort based on a function of each item   	key=lambda x: len(x)

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda word: len(word))

print(f"using (sorted) with lambda, sorted words are   : {sorted_words}")

# ==============================================================
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda x:  len(x[0])>3 and len(x[1])>3,list(zip(l1,l2))))

print(opposites)








species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species,population))
endangered = list(filter(lambda x: x[1]<2500,pop_info))
