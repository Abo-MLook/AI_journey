import sys
from logging import exception


def show_balance():
         print(f"You balance now is ${balance}")

def withdraw():
    global balance
    try:
        price = float(input("Enter the price you want to withdraw : "))
        if price < 0:
            print("Enter number more then zero")
            return
        if balance < price:
            print(f"your balance is less then you are trying to withdraw\n{show_balance()}")
            return
        balance -= price
        print(f"Successfully withdraw ${price}\n{show_balance()}")
        return

    except ValueError:
        print("please enter numbers only")



def deposit():
    global balance
    try:
        price = float(input("Enter the price you want to deposit : "))
        if price < 0:
            raise exception("Enter number more then zero")
        balance += price
        print(f"Successfully deposit ${price}\n{show_balance()}")
        return

    except ValueError:
        print("please enter numbers only")



balance = 0.0

while True:

    print("Banking program : ")
    print("\n1- show balance")
    print("2- Withdraw")
    print("3- Deposit")
    print("q to exit")

    choice = input("choose : ")
    match choice:
        case "1":
            show_balance()

        case "2":
            withdraw()

        case "3":
            deposit()

        case "q":
            sys.exit("exited..")
        case _: print("invalid option, please choose again")


