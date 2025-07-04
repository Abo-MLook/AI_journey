

def printing(name):
    print(f"Hello this is {name}\nat noon we are going to play Grounded please be there")
    print("do not forget to install it before")


def seq(num):
    return num * num

def print_full_name(first , last):
   print(f"{first}",f"{last}",sep=" | ") # sep is meaning separated with

printing("MRWAN")

z = input("ENTER A NUMBER : ")
g = seq(float(z))
print(g)

print_full_name( last="Alayed",first= "Mrwan") # passing using keyword

#---------------------------------------------------------------------------------------------
#           ARBITRARY:
# *args = allows you to pass multiple non-key arguments, it add the passing parameters inside a tuple; can accept any type
# **kwargs = allows you to pass multiple keyword-arguments, it add the passing parameters inside a dictionary; can accept any type

# *args = allows you to pass multiple non-key arguments, it add the passing parameters inside a tuple; can accept any type
print("\n\n")
def adding_lotsNumber(*numbers):
    total = 0
    print(type(numbers))
    for number in numbers:
        total += number

    return total

print(adding_lotsNumber(1,2,3,4,5,6))

print("\n\n")
# **kwargs = allows you to pass multiple keyword-arguments, it add the passing parameters inside a dictionary; can accept any type
def print_StudentInfo(**informatinos):
    print(type(informatinos))

    for key , item in informatinos.items():
        print(f"{key} : {item}")


print_StudentInfo(id="431107769",name = "MRWAN FAHAD ALAYED",age = 22, GPU = 4.98 , collage = "computer collage")