import argparse as ar
import sys

import guess_number as guess_game
import rps




def arcade(name):


    print(f"{name} welcome to the arcade game 🎉🎉🎉!!")
    while True:
        choose = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nor press 'x' to exit the Arcade\n\nYour choice : ")

        if choose not in ["1","2","x"]:
            print("please enter only 1 or 2 or 'x' only!")
        elif choose == "1":
            rps_game = rps.rps(name)
            rps_game()
            print(f"\n\n{name}, welcome to the arcade again")

        elif choose =="2":
            guessing_game = guess_game.guessing_number(name)
            guessing_game()
            print(f"\n\n{name}, welcome to the arcade again")

        else:
            print(f"I hope you enjoyed {name} 😁🙌!!")
            sys.exit(f"by {name}, see you again 🎉")

if __name__ == "__main__":
    parser = ar.ArgumentParser(
        description="Welcome to the arcade !!"
    )
    parser.add_argument(
        "-n", "--name", metavar="name"
        , required=True, help="The name of the player"
    )
    player = parser.parse_args()
    game =arcade(player.name)