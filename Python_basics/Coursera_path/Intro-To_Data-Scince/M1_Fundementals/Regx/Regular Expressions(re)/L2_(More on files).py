import re

# ======================================================================= matching from file
with open("Data.txt","r") as f:
    content = f.read() # content in Data file inside content var now

    pattern = re.compile(r"\d{3}[-.]\d{3}[-.]\d{4}") # the pattern you want to search // [-.] match a - or .

    matchs = pattern.finditer(content)  # searching the pattern inside and store it inside matchs

    #for match in matchs:
    #    print(match)
print()
#-------------------------------------------------------------exit

# ======================================================================= searching for mat pat ... except bat or capital

with open("Data.txt","r") as f:
    content = f.read() # content in Data file inside content var now

    pattern = re.compile(r"[^bA-Z]at") # any letters that is not start with b and capital .

    matchs = pattern.finditer(content)  # searching the pattern inside and store it inside matchs

    #for match in matchs:
    #    print(match)


print()
#-------------------------------------------------------------exit


# ====================================================== search on  any string with (Mr name) or (Mr. name)
with open("Data.txt","r") as f:
    content = f.read() # content in Data file inside content var now

    pattern = re.compile(r"Mr\.?\s[A-Z]\w*") # match string start with Mr and . or space then Capital letter then 0 or more letters
    pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*") # match string start with Mr or Mrs or Ms and . or space then Capital letter then 0 or more letters
 
    matchs = pattern.finditer(content)  # searching the pattern inside and store it inside matchs

    for match in matchs:
       print(match)

print()
#-------------------------------------------------------------exit


# ======================================================================= matching from file


print()
#-------------------------------------------------------------exit