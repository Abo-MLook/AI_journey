first = input("enter your first name : ")
last = input("enter your last name : ")

print(f"welcome {first + last}")

print()
print(f"The last letter of each string , first name :{first[-1]} , the last name :{last[-1]}")
print()
first = first.capitalize()
last =last.capitalize()
print(first + " " +  last)
print()

name = first + " "  +  last
print("O is there" if name.find("O")!=-1 else "it is not there")
print()
print(first[1:-1])
print(last[1:-1])
print()
print(first[-3:] * 3)
print(last[-3:] * 3)