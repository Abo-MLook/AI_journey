import sys
import random
from enum import Enum

def rps():
    game_count = 0 # used global var
    player_wins = 0
    python_wins= 0
    player_draws = 0

    def play_rps():
        # to access them
        nonlocal game_count
        nonlocal player_wins
        nonlocal python_wins
        nonlocal player_draws


        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )
        def winner(player , computer):
            nonlocal player_wins
            nonlocal player_draws
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins +=1
                return "🎉 You win!"

            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                player_draws += 1
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = winner(player,computer) # used nested function
        print(game_result)
        game_count += 1
        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"you played {game_count} times")
            print(f"Your wins {player_wins}")
            print(f"Your losts {python_wins}")
            print(f"Your draws {player_draws}")

            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_rps
rock_paper_scissors = rps() # play now have access on the vars and can call play rps

if __name__ == "__main__": # if the main file ranning execute the play , other if it is from improting do not execute
    rock_paper_scissors()