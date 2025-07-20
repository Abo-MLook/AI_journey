import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


# ======================================================================= matching from file
pattern = re.compile(r'')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

print()
#-------------------------------------------------------------exit