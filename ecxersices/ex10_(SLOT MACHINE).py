import random
import sys
from random import choice


class Invalid_bet(Exception):
    pass

def getBet(balence):
    while True:
        try:
            bet = int(input("Enter your bet amount as a number : "))
            if bet > balence:
                raise Invalid_bet("The bet is more then you have")
            return bet
        except ValueError:
            print("Enter number please !!")

        except Invalid_bet as invalid:
            print(invalid)

def complate():
    while True:
        try:
            user_dis = input("do you want to play (Y/N)")
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
               "3": "🍋",
               "4": "🔔",
               "5": "⭐", }
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



            print("*********")
            for x in user_luck:
                print(f"{machine.get(x)}",end=" | ")

            print()
            print("*********")

            if user_luck[0] == user_luck[1] == user_luck[2]:
                print(f"Wow,{name}, you won !!!")
                balence += bet
            else:
                print(f"Sorry,{name}, you lost !!!")
                balence -= bet

            choice = complate()
            if choice == "y":
                continue
            elif choice == "n":
                sys.exit("exiting..")



    return start


user = playing()
user()
















