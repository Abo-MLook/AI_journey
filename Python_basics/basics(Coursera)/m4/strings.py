ss = "    Hello, World    "

els = ss.count("l")
print(els)

print(ss)
print(ss.strip())
print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

news.replace("***","0")
print(news)


print()
food = "banana bread"
print(food.upper())
print()

#what is the output :
s = "python rocks"
print(s[1]*s.index("n"))
## //

print()

# string format :
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))
