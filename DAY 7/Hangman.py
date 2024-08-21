from random import *

words = ["aarvdark", "baboon", "camel"]



def make_placeHolder(target, placeholder):
    for letter in target:
        placeholder.append("_")




def start():
    ans = game()
    print(ans)
    

def game():
    placeholder = []
    chances = 0
    right_guess = False
    target = choice(words)
    make_placeHolder(target,placeholder)
    print(target)
    while True:
        if chances == 6:
            return "You lost"
        guess = input("Guess a letter of the word: ").lower()
        for letter in range(len(target)):
            if guess == target[letter]:
                placeholder[letter] = guess
                right_guess = True
        if right_guess == False:
            chances += 1
        right_guess = False
        if "".join(placeholder) == target:
            return "You win"
        print("".join(placeholder))


start()
