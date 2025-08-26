import random

choices1 = ("paper" , "rock" , "scissor")


rounds = int(input("Enter how many round in the game : "))
points = 0
for x in range(0 , rounds):
    print(f"ROUND {x + 1} :\n")
    real = random.choice(choices1)
    while True:
      guess = input("Enter a play guess (paper) - (rock) - (scissor) : ")
      if guess.lower() != "paper" and  guess.lower() != "rock" and guess.lower() != "scissor":
          print("you did not enter any from given")
          continue
      else:
          break

    if guess == real:
        print(f"Your combative play : {real}\t\tYOU DRAW THIS ROUND")
        points += 1

    elif guess =="paper" and real =="rock":
        print(f"Your combative play : {real}\t\tYOU WON THIS ROUND")
        points += 3

    elif guess =="scissor" and real == "paper" :
        print(f"Your combative play : {real}\t\tYOU WON THIS ROUND")
        points += 3

    elif guess =="rock" and real == "scissor" :
        print(f"Your combative play : {real}\t\tYOU WON THIS ROUND")
        points += 3

    else:
        print(f"Your combative play : {real}\t\tYOU LOST THIS ROUND")


    print()
print("---------------------------")
print(f"|\tYour total points {points}\t|")
print("---------------------------")
