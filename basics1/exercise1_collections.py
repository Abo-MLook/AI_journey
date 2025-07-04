
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
        price = float(input(f"Enter the price of {food}'s food in dolar : "))
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
for x in range (0 , len(foods)):
    print(f"\t{foods[x]:^5}\t\t|\t\t{prices[x]:^5.2f}$")

print("\t    \t\t|")
print("____________________________")
print(f"\tTOTAL\t\t|\t\t{total:.2f}$")
