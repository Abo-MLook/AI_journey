
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want   (q to exit) : ")
    if food.lower() == "q":
        break
    elif food.isdigit():
        while food.isdigit():
            food = input("Do not enter numbers please the name of food you want : ")

    while True:
     try:
        price = float(input(f"Enter the price of {food}'s food in dollar : "))
        break
     except ValueError:
            print(f"Enter the price of {food}'s food as number not characters !! ")
    total += price
    foods.append(food)
    prices.append(price)

print("\n\n\n")
print("\t-------YOUR CART-------\n")
print("\tFOOD\t\t|\t\tPRICE")
print("____________________________")
#for x  in range (0 , len(foods)):         work ✅
#    print(f"\t{foods[x]:^5}\t\t|\t\t{prices[x]:^5.2f}$")

#for x ,y in foods , prices:               not work 🚫         :       for x, y in (["Pizza", "Water"], [1.0, 2.0]):
#    print(f"\t{x:^5}\t\t|\t\t{y:^5.2f}$")

for x ,y in zip(foods , prices):               # work ✅         :     zip(foods, prices) → [("Pizza", 1.0), ("Water", 2.0)]
    print(f"\t{x:^5}\t\t|\t\t{y:^5.2f}$")

print("\t    \t\t|")
print("____________________________")
print(f"\tTOTAL\t\t|\t\t{total:.2f}$")

print("\n\n===========\n")
# The zip() function in Python combines two or more iterables (like lists or tuples) into pairs (tuples), element by element.

# using zip to create dictionary :
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 22]

person_dict = zip(names, ages)

person_dict = dict(person_dict)
print(person_dict)