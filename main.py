import os
from words import word_list
import hangman

#Introduction About the game

while True:
    print("This game created by ARYAN SHARMA")
    print("---------WELLCOME TO HANGMAN GAME----------")
    print ()
   #player will type name
    player = input("Enter your name ")
    print ("Hello, " + player, "Time to play hangman!")
    # The Game Menu
    print()
    print("Let's Play Hangman game ")
    print("Enter 1 to play version 2.0 of hangman")
    print("Enter 2 to get to know about game")
    print("Enter 3 to word help game")
    print("Enter 4 to play version 1.0 of hangman")
    print("Enter 5 to quit the game")
    print()
     
 
    # player will decide 
    try:
        Choice = int(input("Enter your choice = "))
    
    except ValueError:
        clear()
        print("Wrong Choice")   
        continue
 
    # player want to version 2.0 of hangman
    if Choice == 1:
        os.system('python hangman.py')
        
        
    # player want to know about the game
    elif Choice == 2:
       print("This game test how much you know about india and there states and capitals name ")
       print("you may 6 chance to complete the game if you guess wrong 1 chance will be remove be careful")
       print("")
       
           
    # player want to know about the game
    elif Choice == 3:
        print("words",word_list)
        
    # player want to know about the game
    elif Choice == 4:
        os.system('python h.py')
        
    # player want to quit the game
    
       
