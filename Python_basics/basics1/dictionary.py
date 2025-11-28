
best_food = {"Burger days": "Vaiolit burger",
             "Burger hunsh": "Smoky burger",
             "Calafornia Burger": "clasic burger",
             "Makdonaldez": "Big tasty"}

# print(dir(best_food))
# print(help(best_food))
print("Burger days" in best_food)
print("Vaiolit burger" in best_food)

print(best_food["Burger days"])
print(best_food.get("Burger days"))

best_food.update({"Burger days": "Volcano burger"})
best_food.update({"Hardeze": "Mashrom burger"})
print(best_food)
best_food.popitem()
best_food.pop("Burger days")
print(best_food)
print()
print()
print("--------------------")
for x in best_food.keys():
    print(f"{x} : {best_food[x]} ")
print()
print()
for key, item in best_food.items():
    print(f"{key} : {item}")

# The zip() function in Python combines two or more iterables (like lists or tuples) into pairs (tuples), element by element.

# using zip to create dictionary :
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 22]

# [("Alice", 24), ("Bob", 30), ("Charlie", 22)] zip to list
person_List = list(zip(names, ages))
print(person_List)
# {"Alice": 24, "Bob": 30, "Charlie": 22} zip to dictionary
person_dict = dict(zip(names, ages))

print((person_dict))
