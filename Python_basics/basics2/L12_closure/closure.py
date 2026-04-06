# A closure is a function that remembers the values from its enclosing lexical scope,
# even if the outer function has finished executing.

# In Python, closures happen when:
# 1- A nested function is defined inside another function.
# 2- The inner function uses variables from the outer function.
# 3- The outer function returns the inner function.

def parent_function(person_name, coin=3):
    # coin = 3

    def child_function():  # has access on elements in parent
        nonlocal coin
        coin -= 1

        if coin > 1:
            print(f"{person_name} has {coin} coins left.")
        elif coin == 1:
            print(f"{person_name} has {coin} coin left.")
        else:
            print(f"{person_name} is out of coins")
            #! we did not write person_name as nonlocal because we want to just access it to print not modify , to modify we must put nonlocal

    return child_function  # without () so it can be used directly in main


# save the name but return the function inside so can be used down
ob = parent_function("Mrwan")
ob()
ob()
ob()
