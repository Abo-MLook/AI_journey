#   Set = {} unordered and mutable , but Add/Remove OK. NO duplicates , it is implemnted as hash table so finding is O(1)
#
#
#  Supports powerful operations like:
# union (|)
# intersection (&)
# difference (-)
# symmetric_difference (^)
# These are useful in mathematics, filtering, and data analysis.

game = {"rock", "d", "paper", "scissors"}

print(game)

for x in game:
    print(x, end="  < -  ")

print()
# print(dir(game))
# print(help(game))

print(len(game))
print("halo" in game)
game.add("halo")
print("halo" in game)
game.remove(game[0])
print(game)
