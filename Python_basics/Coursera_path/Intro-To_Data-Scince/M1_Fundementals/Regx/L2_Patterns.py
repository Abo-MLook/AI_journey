import re

# Let's talk more about patterns and start with character classes. Let's create a string of a single learners'
# grades over a semester in one course across all of their assignments
grades="ACAAAABCBCBAA"

# If we want to answer the question "How many B's were in the grade list?" we would just use B
print(re.findall("B",grades))

# If we wanted to count the number of A's or B's in the list, we can't use "AB" since this is used to match
# all A's followed immediately by a B. Instead, we put the characters A and B inside square brackets
print(re.findall("[AB]",grades))

# This is called the set operator. You can also include a range of characters, which are ordered
# alphanumerically. For instance, if we want to refer to all lower case letters we could use [a-z] Lets build
# a simple regex to parse out all instances where this student receive an A followed by a B or a C
print(re.findall("[A][B-C]",grades))

# Notice how the [AB] pattern describes a set of possible characters which could be either (A OR B), while the
# [A][B-C] pattern denoted two sets of characters which must have been matched back to back. You can write
# this pattern by using the pipe operator, which means OR
print(re.findall("AB|AC",grades))


# We can use the caret with the set operator to negate our results.
# For instance, if we want to parse out only
# the grades which were not A's
print(re.findall("[^A]",grades))


# Note this carefully - the caret was previously matched to the beginning of a string as an anchor point, but
# inside of the set operator the caret, and the other special characters we will be talking about, lose their
# meaning. This can be a bit confusing. What do you think the result would be of this?
print(re.findall("^[^A]",grades))


# It's an empty list, because the regex says that we want to match any value at the beginning of the string
# which is not an A. Our string though starts with an A, so there is no match found. And remember when you are
# using the set operator you are doing character-based matching. So you are matching individual characters in
# an OR method.