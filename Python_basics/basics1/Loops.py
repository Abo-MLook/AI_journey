
print("This is calculator to sum pos and neg numbers enter E to end ")
sum = 0
num = 0
while True:
    num = input("enter a number  E to end : ")

    if num.upper() == "E":
        break

    try:
        num = float(num)
        sum += num
    except ValueError:
        print("error enter numbers only")
print(f"The sum is : {sum:.2f}")


for x in range(1, 11):
    print(f"{x}^2 = {x ** 2}", end="\n------- \n")
