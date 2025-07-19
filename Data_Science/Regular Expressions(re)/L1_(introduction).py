import re
# A regex object in Python is an object that represents a compiled regular expression pattern.

print("\t Tab")
print(r"\t Tab")

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com
,
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
,
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


pattern = re.compile(r'abc') # creates a regex object that looks for the sequence of characters

# finditer() is a method of the regex object (pattern) that searches for
# all non-overlapping matches of the regex pattern in the given string (text_to_search).
matchs = pattern.finditer(text_to_search)  # give span (1,4) for abc which is the index of it, and it is case sensetive so ABC is not include

for match in matchs:
    print(match)

print(text_to_search[1:4])
#============================
pattern = re.compile(r'\\')  # we are looking to (.) without \ before it will be an issue
matchs = pattern.finditer(text_to_search)
for match in matchs:
    print(match)












# example1 :
#text = "My email is example@example.com"
#pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
#match = re.search(pattern, text)
#if match:
#    print(f"Found email: {match.group()}")


#example 2 :
#text = "There are 3 apples and 5 bananas."
#result = re.sub(r'\d+', 'number', text)  # Replaces all numbers with "number"
#print(result)  # Output: There are number apples and number bananas.