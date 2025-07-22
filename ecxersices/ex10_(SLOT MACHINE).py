import random
import sys
from random import choice
#using function,exception,list,dictionary, join method and indexing

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

class Invalid_bet(Exception):
    pass

def getBet(balence):
    while True:
        try:
            bet = int(input("Enter your bet amount as a number : "))
            if bet > balence or bet <= 0:
                raise Invalid_bet("The bet is more then you have or less then 0")
            return bet
        except ValueError:
            print("Enter number please !!")

        except Invalid_bet as invalid:
            print(invalid)

def complate():
    while True:
        try:
            user_dis = input("do you want to play (Y/N) : ")
            if user_dis.lower() == "y" or user_dis.lower() == "n" :
                return user_dis

            else:
                print("Enter a char Y or N please")
        except ValueError:
            print("Enter a char Y or N please")

        except Invalid_bet as invalid:
            print("Enter a char Y or N please")




def playing():
    name = input("please enter your name : ")

    machine = {"1": "🍒",
               "2": "🍉",
               "3": "🍋" }
    balence = 100

    def start():
        nonlocal balence
        print(
            f"****************\n{name} welocme to Python slot machine\nSymbols: {" ".join(machine.values())}\n****************\n")

        while True:

            user_luck = []
            print(f"Your current balance is {balence}$")

            bet = getBet(balence)
            print("spinning...")
            for x in range(3):
                user_luck.append((random.choice(list(machine.keys()))))


            print("Result:")
            print("*********")
            print(" | ".join(machine.get(x) for x in user_luck))


            print()
            print("*********")

            if user_luck[0] == user_luck[1] == user_luck[2]:
                print_color(f"Wow,{name}, you won  🎉🎉🎉🎉🎉🎊🎊🎊!!!","32")
                balence += bet * 3
            else:
                print_color(f"Sorry,{name}, you lost !!!","31")
                balence -= bet

            choice = complate()
            if choice == "y":
                continue
            elif choice == "n":
                sys.exit("exiting..")



    return start


user = playing()
user()
















