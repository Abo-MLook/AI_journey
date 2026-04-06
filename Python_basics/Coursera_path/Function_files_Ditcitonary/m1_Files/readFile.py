f = open("for_reading.txt","r")
entire_file = f.read()
f.close()

f = open("for_reading.txt","r")
entire_file_line = f.readline()
f.close()

print(entire_file) #print whole
print()
print(entire_file_line)#print only first line

print()
f = open("for_reading.txt","r")
entire_file_lines = f.readlines() # return list with \n for each
print(entire_file_lines)
print()
# usually used with for loop
for line in entire_file_lines:
    print(line)
f.close()

print()

# use with usuall to open a file , close by it self

with open("for_reading.txt","r") as f:
    print(f.read())

print()

with open("for_reading.txt","r") as f:
    for line in f:
        print(line)
"""
with open("../m5_sorting","r") as f: # going up one level ../
    print(f.read())
"""


"""
This code demonstrates several ways to read text files in Python and highlights the 
differences between `.read()`, `.readline()`, `.readlines()`, and using `with` blocks.

File Reading Methods:
- `f.read()` → returns the *entire file* as one string.
- `f.readline()` → returns a *single line* (the next unread line).
- `f.readlines()` → returns a *list of all lines*, each ending with a newline character.

Iterating Through Lines:
- After calling `.readlines()`, you can loop over the list to process each line.
- Alternatively, looping directly over the open file object yields lines one by one, 
  which saves memory for large files.

Using `with` Statements:
- `with open(...) as f:` automatically closes the file when the block ends.
- This is the recommended way to handle files safely and cleanly.

Relative File Paths:
- `"../m5_sorting"` shows using `..` to navigate up one directory level.

Summary:
Python provides flexible tools for reading files—either whole, line-by-line, or as lists—
and `with` statements ensure proper cleanup without manually calling `close()`.
"""
