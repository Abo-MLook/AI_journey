import re


with open("ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()


# Ok, this works, but it's a bit of a pain. To this point we have been talking about a regex as a single
# pattern which is matched. But, you can actually match different patterns, called groups, at the same time,
# and then refer to the groups you want. To group patterns together you use parentheses, which is actually
# pretty natural. Lets rewrite our findall using groups
print(re.findall("([\w ]*)(\[edit\])",wiki))

print()

# Nice - we see that the python re module breaks out the result by group. We can actually refer to groups by
# number as well with the match objects that are returned. But, how do we get back a list of match objects?
# Thus far we've seen that findall() returns strings, and search() and match() return individual Match
# objects. But what do we do if we want a list of Match objects? In this case, we use the function finditer()
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())


print()

# We see here that the groups() method returns a tuple of the group. We can get an individual group using
# group(number), where group(0) is the whole match, and each other number is the portion of the match we are
# interested in. In this case, we want group(1)
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))

print()


# One more piece to regex groups that I rarely use but is a good idea is labeling or naming groups. In the
# previous example I showed you how you can use the position of the group. But giving them a label and looking
# at the results as a dictionary is pretty useful. For that we use the syntax (?P<name>), where the parethesis
# starts the group, the ?P indicates that this is an extension to basic regexes, and <name> is the dictionary
# key we want to use wrapped in <>.
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict()['title'])

print()
# Of course, we can print out the whole dictionary for the item too, and see that the [edit] string is still
# in there. Here's the dictionary kept for the last match
print(item.groupdict())

# Ok, we have seen how we can match individual character patterns with [], how we can group matches together
# using (), and how we can use quantifiers such as *, ?, or m{n} to describe patterns. Something I glossed
# over in the previous example was the \w, which standards for any word character. There are a number of
# short hands which are used with regexes for different kinds of characters, including:
# a . for any single character which is not a newline
# a \d for any digit
# and \s for any whitespace character, like spaces and tabs
# There are more, and a full list can be found in the python documentation for regexes

print()
# One more concept to be familiar with is called "look ahead" and "look behind" matching. In this case, the
# pattern being given to the regex engine is for text either before or after the text we are trying to
# isolate. For example, in our headers we want to isolate text which  comes before the [edit] rendering, but
# we actually don't care about the [edit] text itself. Thus far we have been throwing the [edit] away, but if
# we want to use them to match but don't want to capture them we could put them in a group and use look ahead
# instead with ?= syntax
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    # What this regex says is match two groups, the first will be named and called title, will have any amount
    # of whitespace or regular word characters, the second will be the characters [edit] but we don't actually
    # want this edit put in our output match objects
    print(item)
