import re
grades="ACAAAABCBCBAA"

# Ok, so we've talked about anchors and matching to the beginning and end of patterns. And we've talked about
# characters and using sets with the [] notation. We've also talked about character negation, and how the pipe
# | character allows us to or operations. Lets move on to quantifiers.

# Quantifiers are the number of times you want a pattern to be matched in order to match. The most basic
# quantifier is expressed as e{m,n}, where e is the expression or character we are matching, m is the minimum
# number of times you want it to matched, and n is the maximum number of times the item could be matched.

# Let's use these grades as an example. How many times has this student been on a back-to-back A's streak?
print(re.findall("A{2,10}",grades) )# we'll use 2 as our min, but ten as our max

# So we see that there were two streaks, one where the student had four A's, and one where they had only two
# A's

# We might try and do this using single values and just repeating the pattern
print(re.findall("A{1,1}A{1,1}",grades))

# As you can see, this is different than the first example. The first pattern is looking for any combination
# of two A's up to ten A's in a row. So it sees four A's as a single streak. The second pattern is looking for
# two A's back to back, so it sees two A's followed immediately by two more A's. We say that the regex
# processor begins at the start of the string and consumes variables which match patterns as it does.

# It's important to note that the regex quantifier syntax does not allow you to deviate from the {m,n}
# pattern. In particular, if you have an extra space in between the braces you'll get an empty result
print(re.findall("A{2, 2}",grades))

# And as we have already seen, if we don't include a quantifier then the default is {1,1}
print(re.findall("AA",grades))


# Oh, and if you just have one number in the braces, it's considered to be both m and n
print(re.findall("A{2}",grades))

# Using this, we could find a decreasing trend in a student's grades
print(re.findall("A{1,10}B{1,10}C{1,10}",grades))



