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
print()
#-------------------------------------------------------------exit

#============================================================================ other example
pattern = re.compile(r'\\')  # we are looking to (.) without \ before it will be an issue, it will give all chars
matchs = pattern.finditer(text_to_search)
for match in matchs:
    print(match)


print()
#-------------------------------------------------------------exit

#============================================================================ using ways to search , from snippets.txt
# chick snippets.txt
# I want to search  mr. name
pattern = re.compile(r'\w\w\w*\.\s\w+') # and so on from the symbols from file......
matchs = pattern.finditer(text_to_search)
for match in matchs:
    print(match)


pattern = re.compile(r'\d+-\d+-\d+') # and so on from the symbols from file......
matchs = pattern.finditer(text_to_search)
for match in matchs:
    print(match)
    print()
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # and so on from the symbols from file......
matchs = pattern.finditer(text_to_search)
for match in matchs:
    print(match)

print()
#-------------------------------------------------------------exit


