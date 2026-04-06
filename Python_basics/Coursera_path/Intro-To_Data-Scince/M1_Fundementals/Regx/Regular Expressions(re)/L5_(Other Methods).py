import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

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

# ======================================================================= findall method
# findall return matchs as list of string
# if there is more then one group it return  tuples of each one
print("findall method:")

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matchs = pattern.findall(text_to_search)

for match in matchs:
    print(match)
print()
#-------------------------------------------------------------exit

# ======================================================================= match method
# return match of specific string if it is in the beginning  , if it is not return none
print("match method:")
sentence = 'Start a sentence and then bring it to an end'
pattern1 = re.compile(r'Start')
matchs1 = pattern1.match(sentence)

pattern2 = re.compile(r'then')
matchs2 = pattern2.match(sentence)

print(matchs1)
print(matchs2)

print()
#-------------------------------------------------------------exit

# ======================================================================= search method
# same is match,but it match even if not at start of string
print("search method:")
sentence = 'Start a sentence and then bring it to an end'
pattern1 = re.compile(r'Start')
matchs1 = pattern1.search(sentence)

pattern2 = re.compile(r'then')
matchs2 = pattern2.search(sentence)

print(matchs1)
print(matchs2)

print()
#-------------------------------------------------------------exit