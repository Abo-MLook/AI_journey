# r = Read
# a = Append
# W = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt" , "r") # even if we did not put "r" the default is read for open
print(f.read()) # print all file
# print(f.read()) This will not print anything, The file already read and it is in end of file now

# print(f.read(4)) will print the first 4 letters

print(f.readlines()) # print line
# print(f.readlines()) print the second line

for line in f:
    print(line)

f.close()

# Nice structure for opening a file:
try:
    f = open("names.txt")
    for line in f:
        print(line)
except:
    print("The file you want to read is not there")

finally:
    f.close()

#=======================
# a = Append : create the file if it doesn't exist , used to modify a file of create one
f = open("names.txt","a")
f.write("Turky")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# other good method :
f = open("names.txt","a+") # a+ append and read
f.write("Sabhan")
f.seek(0) # go back to the beginning of the file
print(f.read())
