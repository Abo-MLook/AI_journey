import  random
from logging import exception


class valied_guess(Exception):
    pass

words = ("apple", "orange", "banana", "cocount")



hangman_art =  {0:("   ",
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
    pass

def display(hint):
    pass

def display_answer(answer):
    pass

def get_guess():
    while True:
        try:
            guess = chr(input("Enter a letter"))
            return guess
        except ValueError:
            print("Please enter one letter")
def main():
    answer = random.choice(words)
    hent = ["_"] * len(answer)
    wrong_guesses = 0
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display(hent)
        guess = get_guess()

