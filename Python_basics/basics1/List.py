#   List = [] ordered and changeable. Duplicates OK

game = ["rock", "rock", "paper", "scissors"]

print(game)
print(game[0])
print(game[::-1])


for x in game:
    print(x, end="  < -  ")

print()
# ----------- filling empty list
seq = []
for x in range(1, 11):
    seq.append(x * x)
print(seq)
# ----------- same way but flixable way

seq2 = [x * x for x in range(1, 11)]
print(seq2)

seq3 = [x % 2 != 0 for x in range(1, 11)]  # wrong it will be Boolean vaules
print(seq3)

# create list of odd num to 10 , vaule - loop - condition
seq4 = [x for x in range(1, 11) if x % 2 != 0]
print(seq4)

# can not add anything because it is a tuple
seq5 = (x * x for x in range(1, 11))
print(seq5)

# -------------
first_game = [x[0] for x in game]
print(first_game)
# print(dir(game))
# print(help(game))

print(len(game))
print("halo" in game)
game.append("halo")
print("halo" in game)
game.insert(0, "elden")
print(game)
game.reverse()
print(game)
game.clear()
print(game)

# ---
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
positives = [num for num in numbers if num > 0]
print(positives)
