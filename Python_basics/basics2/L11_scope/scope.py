# Scope refers to the area of your code where a variable is recognized and can be used.
name = "Dave"
count = 1


def another():
    color = "blue"
    # count +=1  this will create new var but there is not value to it to add , so error
    global count
    count += 1
    print(count)

    def greeting(name):
        # color = "white" this will create new var with white , not modify the original one
        nonlocal color  # this will modify it
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
