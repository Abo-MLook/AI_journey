import re

"""
The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people
 with their grade in a class. 
Create a regex to generate a list of just those students who received a B in the course.
"""


def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE

    lis = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+:\sB",grades)
    return lis

print(grades())
