import re
# Let's look at some more wikipedia data. Here's some data on universities in the US which are buddhist-based
with open("buddhist.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen


# We can see that each university follows a fairly similar pattern, with the name followed by an – then the
# words "located in" followed by the city and state

# I'll actually use this example to show you the verbose mode of python regexes. The verbose mode allows you
# to write multi-line regexes and increases readability. For this mode, we have to explicitly indicate all
# whitespace characters, either by prepending them with a \ or by using the \s special value. However, this
# means we can write our regex a bit more like code, and can even include comments with #
pattern="""
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in
"""

# Now when we call finditer() we just pass the re.VERBOSE flag as the last parameter, this makes it much
# easier to understand large regexes!
for item in re.finditer(pattern,wiki,re.VERBOSE):
    print(item.groupdict())    # We can get the dictionary returned for the item with .groupdict()
