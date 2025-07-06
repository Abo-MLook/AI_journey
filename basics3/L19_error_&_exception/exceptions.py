# ------------------------------------------
# ERROR vs EXCEPTION
# Error: Crashes the program.
# Exception: Can be handled with try-except to prevent crashing.
# ------------------------------------------


# ------------ version 1 ------------
try:
    print(x)  # ❌ This will raise a NameError (x is not defined)
except:
    print("Error")  # ✅ Generic error handler (not recommended for real programs)

# Output:
# Error

print("\n\n")

# ------------ version 2 ------------
try:
    print(x)  # ❌ Again, x is undefined — raises NameError

# Specific exception handling starts here
except NameError:
    print("name error means somting that is probably undefined")  # ✅ This block runs

except ZeroDivisionError:
    print("error can not be divid on zero")  # ❌ Not triggered

else:
    print("No error")  # ❌ Skipped because error occurred

finally:
    print("This always run")  # ✅ Always executes (cleanup code)

# Output:
# name error means somting that is probably undefined
# This always run

print("\n\n")

# ------------ version 3 ------------
try:
    # Uncomment the line below to raise a manual (custom) exception immediately:
    # raise Exception("finished from try")  # Force error manually

    x = int("hello")  # ❌ Will raise ValueError (invalid literal for int)

    # If no exception is raised above, the code continues:
    if type(x) is not type(str):
        # This block will raise a TypeError if x is not a string
        raise TypeError("only string is allowed")

# Specific exceptions below (in order of priority)
except NameError:
    print("name error means somting that is probably undefined")  # ❌ Not triggered

except ZeroDivisionError:
    print("error can not be divid on zero")  # ❌ Not triggered

# Catch-all for any other exceptions (like ValueError or TypeError)
except Exception as error:
    print("error is : ", error)  # ✅ This runs — handles ValueError from int("hello")

else:
    print("No error")  # ❌ Skipped — exception occurred

finally:
    print("This always run")  # ✅ Always runs

# Output:
# error is :  invalid literal for int() with base 10: 'hello'
# This always run
