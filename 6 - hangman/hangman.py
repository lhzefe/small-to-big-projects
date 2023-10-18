import os, random, time
from modules import game_art
from modules.game_words import list_words

#Game header
os.system("cls")
game_art.hangman_logo()
time.sleep(5)
os.system("cls")
game_art.hangman_lives()

#Choosing the word 
word = list(random.choice(list_words))
hide_word = ["_" for letter in word]
print(f"\n\n\n{" ".join(hide_word)}\n")

#Receiving letter from user and doing the logic
lives = 5
while lives > 0:
    chosen_letter = input("Insert the chosen letter: ").lower()
    if chosen_letter in hide_word:
        print(f"You already insert the letter '{chosen_letter}', please try" +\
            " another letter.")
        time.sleep(3)
    elif chosen_letter in word:
        for letter in range(len(word)):
            if chosen_letter == word[letter]:
                hide_word[letter] = chosen_letter
    else:
        lives-=1
        
    os.system("cls")
    game_art.hangman_lives(lives)
    print(f"\n\n\n{" ".join(hide_word)}\n")

    if hide_word == word:
        print("END GAME. You Win!")
        break

    if lives < 1:
        print("You Lose!")
