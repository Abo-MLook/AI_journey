import random
from logging import exception
# using function,exception,list and indexing


class valied_guess(Exception):
    pass


words = ("apple", "orange", "banana", "caravan")


hangman_art = {0: ("   ",
                   "   ",
                   "   "),

               1: (" o ",
                   "   ",
                   "   "),

               2: (" o ",
                   " | ",
                   "   "),

               3:   (" o ",
                     "/| ",
                     "   "),

               4:  (" o ",
                    "/|\\",
                    "   "),

               5:  (" o ",
                    "/|\\",
                    "/  "),

               6:  (" o ",
                    "/|\\",
                    "/ \\")}


def display_man(wrong_guesses):
    for x in hangman_art[wrong_guesses]:
        print(x)


def display(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(f"The answer is : {answer}")


def get_guess():
    while True:
        try:
            guess = input("Enter a letter : ")
            if not (len(guess) == 1 and guess.isalpha()):
                raise valied_guess("Please enter one letter")
            return guess
        except valied_guess as v:
            print(v)


def complate():
    try:
        choose = input("do you want to play again ?  Y/N : ")
        if choose.lower() not in ["y", "n"]:
            raise valied_guess("please enter  Y or N")
        return choose
    except valied_guess as v:
        print(v)


def main():
    answer = random.choice(words)
    hent = ["_"] * len(answer)
    wrong_guesses = 0
    right_guesses = 0

    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display(hent)
        guess = get_guess()

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess and hent[index] == "_":
                    hent[index] = guess

        if "_" not in hent:
            display_man(wrong_guesses)
            print("YOU won!!")
            display_answer(answer)
            break

        else:
            print("not there !!")
            wrong_guesses += 1

        if wrong_guesses == 6:
            print("Sorry your lost")
            display_man(wrong_guesses)
            is_running = False

    choose = complate()
    if choose == "y":
        main()
    else:
        print("thank you for playing")


if __name__ == "__main__":
    main()
