

best_food = {"Burger days":"Vaiolit burger",
             "Burger hunsh":"Smoky burger",
               "Calafornia Burger" : "clasic burger",
                 "Makdonaldez":"Big tasty"}

#print(dir(best_food))
#print(help(best_food))
print("Burger days" in best_food)
print(best_food["Burger days"])
print(best_food.get("Burger days"))

best_food.update({"Burger days": "Volcano burger"})
best_food.update({"Hardeze": "Mashrom burger"})
print(best_food)
best_food.popitem()
best_food.pop("Burger days")
print(best_food)

for x in best_food.keys():
    print(f"{x} : {best_food[x]} ")
print()
print()
for key , item in best_food.items():
    print(f"{key} : {item}")