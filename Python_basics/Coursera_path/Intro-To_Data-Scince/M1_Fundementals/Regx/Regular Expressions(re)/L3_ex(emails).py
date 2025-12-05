import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
# ======================================================================= matching first email
pattern = re.compile(r'[a-zA-Z]+@[a-z]+\.com')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
print()
#-------------------------------------------------------------exit
# ======================================================================= matching second email
pattern = re.compile(r'[a-z]+.[a-z]+@[a-z]+\.edu')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
print()
#-------------------------------------------------------------exit
# ======================================================================= matching third email
pattern = re.compile(r'[a-z]+-\d+-[a-z]+@[a-z]+-[a-z]+\.net')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
print()
#-------------------------------------------------------------exit

# ======================================================================= matching first two emails
pattern = re.compile(r'[a-zA-Z.]+@[a-z]+\.(com|edu)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
print()
#-------------------------------------------------------------exit

# ======================================================================= matching all emails
pattern = re.compile(r'[a-zA-Z\d.\-]+@[a-z\-]+\.(com|edu|net)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
print()
#-------------------------------------------------------------exit