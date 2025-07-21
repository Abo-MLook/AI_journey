import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# ======================================================================= matching all urls
pattern = re.compile(r'https?://(www\.)?\w+.\w+')
matches = pattern.finditer(urls)

for match in matches:
     print(match)
print()
#-------------------------------------------------------------exit

# ======================================================================= match using group

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # divide it to groups using ( )
# group(0) =  whole email (https?://(www\.)?(\w+)(\.\w+))
# group(1) =  (www\.)
# group(2) =  (\w+)
# group(3) =  (\.\w+)

matches = pattern.finditer(urls)

for match in matches:
     print(f" url : {match.group(0)}\t {match.group(1)}\t "
           f"{match.group(2)}\t {match.group(3)}")
print()
#-------------------------------------------------------------exit

# ======================================================================= match using substituting
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # divide it to groups using ( )
sub_urls = pattern.sub(r'\2\3',urls)  # take from pattern that searched in ulrs data,
# then replace the group 2 and 3 inside this var

print(sub_urls) # print all of them , only group 2 and 3 of each one

print()
#-------------------------------------------------------------exit