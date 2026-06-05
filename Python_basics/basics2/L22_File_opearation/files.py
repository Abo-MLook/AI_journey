import os

# r = Read
# a = Append
# W = Write
# x = Create

# Read - error if it doesn't exist

# even if we did not put "r" the default is read for open
f = open("names.txt", "r")
print(f.read())  # print all file
# print(f.read()) This will not print anything, The file already read and it is in end of file now

# print(f.read(4)) will print the first 4 letters
print("\n=======================1\n")

print(f.readlines())  # print line
# print(f.readlines()) print the second line
print("\n=======================2\n")

for line in f:
    print(line)

f.close()
print("\n=======================3\n")

# Nice structure for opening a file:
try:
    f = open("names.txt")
    for line in f:
        print(line)
except:
    print("The file you want to read is not there")

finally:
    f.close()

print("\n=======================4\n")
# =======================

# a = Append : create the file if it doesn't exist , like adding in file
f = open("names.txt", "a")
f.write("\nTurky")
f.close()
print("\n=======================5\n")

f = open("names.txt")
print(f.read())
f.close()
print("\n=======================6\n")

# other good method :
f = open("names.txt", "a+")  # a+ append and read
f.write(" Sabhan33")
f.seek(0)  # go back to the beginning of the file
print(f.read())
f.close()

print("\n=======================7\n")
# =======================

# W = Write : used to 'Overwrite'
f = open("more_names.txt", "w+")  # w+ write and read
# delete the before text and add this one
f.write("I overwrite the whole file noting exist now before there were names")
f.seek(0)
print(f.read())
f.close()

print("\n=======================8\n")
# =======================

# Wwo ways to create a new file
# 1-  Open a file for writing if exist or (creates )the file if it doesn't exist
f = open("Student_list", "w")  # will create new one or read a file exist
f.close()

print("\n=======================9\n")

# 2-  'Creates' a file if doesn't exist , if it exists will generate error
# using   # x = Create

if not os.path.exists("Bank_names.txt"):
    f = open("Bank_names.txt", "x")
    f.close()


if os.path.exists("Def_names.txt"):
    os.remove("Def_names.txt")
else:
    print("The file you wish to delete does not exist")

print("\n=======================11\n")
# =======================

# meathod better then try and also example for coping file

with open("context.txt") as f:
    content = f.read()

with open("more_names.txt", "w+") as f:
    f.write(str(content))
    f.seek(0)
    print(f.read())
