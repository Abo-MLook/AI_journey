#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#   List = [] ordered and changeable. Duplicates OK

game = ("rock" , "rock" ,"paper" , "scissors")

print(game)
print(game[0])
print(game[::-1])


for x in game:
    print(x,end="  < -  ")

print()
#print(dir(game))
#print(help(game))

print(len(game))
print("halo" in game)
#can not add anything


