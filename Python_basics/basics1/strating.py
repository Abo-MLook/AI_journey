#Strings
hello = "hello "
name = "my name is Marwan"
liking = " and I like burgers"

print(f"name : {hello}{name} \nliking: {liking}")
print("name",hello,name,"\nliking",liking)

#Integers and float
age = 22
height = 170.8

weight = 64.3
GPA = 4.98
isTrue = True
print(f"I am {age} and with height of {height} , weight of {weight} and GPA of {GPA}")
#----------------------------------------------------------------------------------
#!! Casting ::
print(type(age))

age = float(age)
print(type(age))

age = str(age)
print(type(age))



age = int(float(age))
print(age)

age = bool(age)
print(type(age))
print(age)

