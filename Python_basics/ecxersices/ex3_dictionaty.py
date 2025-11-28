
menu = {"POPCORN": 1.00,
        "HOT DOG": 2.00,
        "GIANT PRETZEL": 2.00,
        "ASST CANDY": 1.00,
        "SODA": 1.00,
        "BOTTLED WATER": 1.00, }

prices = []
cart = {}
total = 0

print("\t\t------MENU-------")
for x, y in menu.items():
    print(f"{x:12}\t|\t\t${y}")

print()
while True:
    food = input("Select which one to order  (q to exit) : ").upper()

    if food.lower() == "q":
        break

    elif food.isdigit():
        print("you entered a numbered!!")
        continue

    elif food not in menu:
        print("you entered something not in the Menu!!")
        continue
    else:
        # Python allows you to add items to a dictionary by setting new keys directly.
        cart[food] = menu[food]
        total += cart[food]


print()
print("\t\t-------YOU CART------")
for x in cart.keys():
    print(f"{x:20}\t|\t\t${cart[x]}")

print(f"Total =  ${total}")
