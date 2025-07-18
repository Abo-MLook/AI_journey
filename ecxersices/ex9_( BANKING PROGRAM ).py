import sys
class InvalidDepositAmount(Exception):
    pass

def show_balance():
    return f"You balance now is ${balance}"

def withdraw():
    global balance
    try:
        price = float(input("Enter the price you want to withdraw : "))
        if price < 0:
            raise InvalidDepositAmount("Please enter a number greater than zero.")

        if balance < price:
            print(f"your balance is less then you are trying to withdraw\n{show_balance()}")
            return
        balance -= price
        print(f"Successfully withdraw ${price}\n{show_balance()}")
        return

    except ValueError:
        print("please enter numbers only")
    except InvalidDepositAmount as e:
        print(e)



def deposit():
    global balance
    try:
        price = float(input("Enter the price you want to deposit : "))
        if price < 0:
            raise InvalidDepositAmount("Please enter a number greater than zero.")
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
            print(show_balance())

        case "2":
            withdraw()

        case "3":
            deposit()

        case "q":
            sys.exit("exited..")
        case _: print("invalid option, please choose again")


