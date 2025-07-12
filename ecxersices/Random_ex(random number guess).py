import  random

guess_num = random.randint(0, 100)

while True:
    try:
        user = int(input("guess the number between  0 - 100 : "))
    except ValueError:
        print("please enter integer number")
        continue

    if guess_num > user:
        print("Number is low , try again")

    elif guess_num < user :
        print("Number is heigh , try again")

    else:
        print(f"you got it right it is indeed {guess_num}")
        break