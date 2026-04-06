import re

# ex 1 -----
# Find a list of all of all of the names in the following string using regex.
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    #answer
    find = re.findall("[A-Z][a-z]*",simple_string)
    return find
names()