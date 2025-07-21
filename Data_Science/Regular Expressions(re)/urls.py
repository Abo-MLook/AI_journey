import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'')


matches = pattern.finditer(urls)

for match in matches:
     print(match.group(3))