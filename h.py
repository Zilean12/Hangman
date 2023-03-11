# hangman game 
import time
import random

print("-----HI WELCOME TO HANGMAN GAME----")
print(" Welcome to version 1.0 of HANGMAN GAME ")
print(" ....YOU HAVE TO GUSS THE BTS MEMEBER NAME....")
print("......GOOD LUCK....")

# player will type name

print("Time to play hangman!")

print("")

# time for starting new fresh game
time.sleep(1)

print("Start..")
time.sleep(0.5)

word = "Jin", "Jungkook", "RM", "Kim Taehyung", "Suga", "Jung Ho-seok"
word = random.choice(word)

guesses = ''

# no. of turn
turns = 9

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
    if failed == 0:
        print("You won")
        break

    print()
    guess = input("guess a character:")

    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose")
            print("word: ",word)
print(" THIS GAME IS CREATED BY ARYAN SHARMA ")
print(" HOPE YOU HAVE ENJOYED  ")
print(" NEW VERSION HAS BEEN RELEASE PLZ TRY THAT ALSO")

