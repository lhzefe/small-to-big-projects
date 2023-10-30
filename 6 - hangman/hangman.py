"""This is a simple hangman game."""
import os
import random
import time
from modules import game_art
from modules.game_words import list_words

# Game header
os.system("cls")
game_art.hangman_logo()
time.sleep(5)
os.system("cls")
game_art.hangman_lives()

# Choosing the word
word = list(random.choice(list_words))
hide_word = ["_" for letter in word]
print(f"\n\n\n{' '.join(hide_word)}\n")

# Receiving letter from user and doing the logic
lives = 5
typed_letters = []
while lives > 0:
    chosen_letter = input("Insert the chosen letter: ").lower()
    if chosen_letter in typed_letters:
        print(f"You already insert the letter '{chosen_letter}', please try" +
              " another letter.")
        time.sleep(3)
    elif chosen_letter in word:
        for index, letter in enumerate(word):
            if chosen_letter == letter:
                hide_word[index] = chosen_letter
    else:
        lives -= 1

    typed_letters.append(chosen_letter)
    os.system("cls")
    game_art.hangman_lives(lives)
    print(f"\n\n\n{' '.join(hide_word)}\n")

    if hide_word == word:
        print("You Win!")
        break

    if lives < 1:
        print(f"The word was '{''.join(word)}'.\nYou Lose!")
