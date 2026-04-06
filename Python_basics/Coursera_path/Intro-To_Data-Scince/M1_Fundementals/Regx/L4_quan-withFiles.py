import re


with open("ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen

# Scanning through this document one of the things we notice is that the headers all have the words [edit]
# behind them, followed by a newline character. So if we wanted to get a list of all of the headers in this
# article we could do so using re.findall
print(re.findall("[a-zA-Z]{1,100}\[edit\]",wiki))

# Ok, that didn't quite work. It got all of the headers, but only the last word of the header, and it really
# was quite clunky. Lets iteratively improve this. First, we can use \w to match any letter, including digits
# and numbers.
print(re.findall("[\w]{1,100}\[edit\]",wiki))


# This is something new. \w is a metacharacter, and indicates a special pattern of any letter or digit. There
# are actually a number of different metacharacters listed in the documentation. For instance, \s matches any
# whitespace character.

# Next, there are three other quantifiers we can use which shorten up the curly brace syntax. We can use an
# asterix * to match 0 or more times, so let's try that.
print(re.findall("[\w]*\[edit\]",wiki))


# Now that we have shortened the regex, let's improve it a little bit. We can add in a spaces using the space
# character
print(re.findall("[\w ]*\[edit\]",wiki))


# Ok, so this gets us the list of section titles in the wikipedia page! You can now create a list of titles by
# iterating through this and applying another regex
for title in re.findall("[\w ]*\[edit\]",wiki):
    # Now we will take that intermediate result and split on the square bracket [ just taking the first result
    print(re.split("[\[]",title)[0])

    """
    This code shows how to iteratively refine a regular expression to extract section 
    headers from a Wikipedia article, using metacharacters and quantifiers.

    Initial Attempt:
    - The wiki text contains headers like:
          Introduction [edit]
    - The pattern `"[a-zA-Z]{1,100}\[edit\]"` only captures the *final word* before “[edit]”.

    Using Metacharacters:
    - `\w` matches letters, digits, and underscore → broader than `[a-zA-Z]`.
    - Updated pattern: `[\w]{1,100}\[edit\]` still captures only one word.

    Using Quantifiers:
    - `*` means “0 or more repetitions”, so:
          "[\\w]*\\[edit\\]"
      matches any contiguous string of word characters before “[edit]”.

    Including Spaces:
    - Adding a space to the character class:
          "[\\w ]*\\[edit\\]"
      lets us capture full multi-word headings.

    Extracting Clean Titles:
    - For each match like "Section Title [edit]", splitting on "[" and taking the first 
      part extracts just the title.

    Summary:
    By progressively expanding the regex using metacharacters (`\w`, `\s`), character 
    classes, and quantifiers (`*`), we can flexibly capture structured patterns such as 
    Wikipedia section headers.
    """
