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