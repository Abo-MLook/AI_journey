import random
import sys


def guessing_number(name):
    counter = 0
    user_wins = 0
    user_lost = 0
    def starting():
        nonlocal name
        nonlocal counter
        nonlocal user_lost
        nonlocal user_wins
        counter += 1
        while True:
            print(f"{name},please enter 1 or 2 or 3 for your guess only these number")
            try:
                user_guess = int(input("guess which number I'm thinking of .. 1 or 2 or 3 :  "))
                if user_guess not in [1,2,3]:
                    print("Enter only 1 or 2 or 3 !!")
                    continue
                break
            except ValueError:
               print("only numbers")

        computer_num =int (random.choice(["1","2","3"]))

        if computer_num == user_guess:
            user_wins +=1
            winning_percentage = float(user_wins / counter) * 100
            print(f"\n{name},you chose {user_guess}.\nI was thinking about number {computer_num} \n\n 🎉{name} , you win! \n\nGame count {counter}\n{name} wins {user_wins}\n"
                  f"{name} ,your winning percentage is {winning_percentage:.2f}%")
        else:
            user_lost +=1

            winning_percentage = float(user_wins / counter) * 100
            print(f"\n{name}, you chose {user_guess}.\nI was thinking about number {computer_num}\n sorry {name} you lost ..😓😓 \n\n\nGame count {counter}\n{name} wins {user_wins}\n"
                  f"{name} , your winning percentage is {winning_percentage:.2f}%")
        while True:
            choice_play = input(f"{name}, do you want to pley again ?\nY for Yes\nQ for Quit\n")
            if choice_play.lower() =="y":
                return starting()
            elif  choice_play.lower() not in ["y","q"]:
                continue
            else:
                print(f"🎉🎉🎉🎉🎉\n{name},Thank you for playing!")
                if __name__ == "__main__":
                    sys.exit(f"\nBye {name} !👋")
                else:
                    print(f"\nBye {name} !👋")
                    return




    return starting

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="welcome to gussing number game"
    )
    parser.add_argument(
        "-n","--name",metavar="name"
        ,required=True,help="Enter you name"
    )
    player = parser.parse_args()
    game = guessing_number(player.name)
    game()