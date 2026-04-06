import re


sentence = 'Start a sentence and then bring it to an end'

# ======================================================================= simple search
print("not using flags:")
pattern1 = re.compile(r'start')
matchs1 = pattern1.search(sentence)

print(matchs1) # it will return none because start in string is Start capital first one
print()
#-------------------------------------------------------------exit

# ======================================================================= using flags
print("using flags:")
pattern1 = re.compile(r'start',re.IGNORECASE) # ignore case flag
matchs1 = pattern1.search(sentence)

print(matchs1)
print()
#-------------------------------------------------------------exit

# there is alot of useful flags , you can search about it 🏋️‍♂️