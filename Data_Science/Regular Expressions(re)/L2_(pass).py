import re

with open("Data.txt","r") as f:
    content = f.read() # content in Data file inside content var now

    pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d") # the pattern you want to search

    matchs = pattern.finditer(content)  # searching the pattern inside and store it inside matchs

    for match in matchs:
        print(match)