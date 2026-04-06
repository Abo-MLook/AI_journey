# First we'll import the re module, which is where python stores regular expression libraries.
import re

# There are several main processing functions in re that you might use. The first, match() checks for a match
# that is at the beginning of the string and returns a boolean. Similarly, search(), checks for a match
# anywhere in the string, and returns a boolean.

# Lets create some text for an example
text = "This is a good day."

# Now, lets see if it's a good day or not:
if re.search("good", text): # the first parameter here is the pattern
    print("Wonderful!")
else:
    print("Alas :(")



# In addition to checking for conditionals, we can segment a string. The work that regex does here is called
# tokenizing, where the string is separated into substrings based on patterns. Tokenizing is a core activity
# in natural language processing, which we won't talk much about here but that you will study in the future

# The findall() and split() functions will parse the string for us and return chunks. Lets try and example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."

# This is a bit of a fabricated example, but lets split this on all instances of Amy
print(re.split("Amy", text))
# You'll notice that split has returned an empty string, followed by a number of statements about Amy, all as
# elements of a list. If we wanted to count how many times we have talked about Amy, we could use findall()
print(re.findall("Amy", text))
print(len(re.findall("Amy", text)))

# Ok, so we've seen that .search() looks for some pattern and returns a boolean, that .split() will use a
# pattern for creating a list of substrings, and that .findall() will look for a pattern and pull out all
# occurences.


# Now that we know how the python regex API works, lets talk about more complex patterns. The regex
# specification standard defines a markup language to describe patterns in text. Lets start with anchors.
# Anchors specify the start and/or the end of the string that you are trying to match. The caret character ^
# means start and the dollar sign character $ means end. If you put ^ before a string, it means that the text
# the regex processor retrieves must start with the string you specify. For ending, you have to put the $
# character after the string, it means that the text Regex retrieves must end with the string you specify.

# Here's an example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."

# Lets see if this begins with Amy
print(re.search("^Amy",text))
print(re.search("succesful.$",text))

# Notice that re.search() actually returned to us a new object, called re.Match object. An re.Match object
# always has a boolean value of True, as something was found, so you can always evaluate it in an if statement
# as we did earlier. The rendering of the match object also tells you what pattern was matched, in this case
# the word Amy, and the location the match was in, as the span.


"""
This code introduces Python’s `re` module and demonstrates how regular expressions 
perform text searching, tokenizing, and pattern matching.

Basic Search Functions:
- `re.search(pattern, text)` finds the first occurrence of a pattern *anywhere* in the string.
- `re.match(pattern, text)` checks only the *start* of the string.
- Example: checking whether a sentence contains the word “good.”

Tokenizing with Regex:
- `re.split(pattern, text)` separates a string based on the pattern.
- `re.findall(pattern, text)` returns all matches as a list.
- Useful for counting, segmenting, and preprocessing text for NLP tasks.

Anchors:
- `^` anchors the pattern to the start of the string.
- `$` anchors the pattern to the end.
- Examples:
      re.search("^Amy", text)
      re.search("successful.$", text)

Match Objects:
- When a match is found, `re.search()` returns a `Match` object.
- This object evaluates to True in conditionals and stores:
      • the matched text  
      • its position (span) in the original string

Summary:
The `re` module offers flexible tools for searching and manipulating text. Anchors, 
tokenizing, and match objects form the basis for more advanced pattern recognition.
"""
