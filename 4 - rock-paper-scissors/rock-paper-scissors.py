import random

rock = r'''
    _______
---'   ___#)
      (#####)
      (#####)
      (####)
---.__(###)
'''
paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (####)
---.__(###)
'''
options = [rock, paper, scissors]
print("This is a Rock, Paper and Scissors game.")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or" +\
                        " 2 for Scissors: \n"))
while user_choice not in range(3):
    print("Your choice is not accept.")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for" +\
                            " Paper or 2 for Scissors: \n"))  
print(options[user_choice])
computer_choice = random.randint(0, 2)
print(options[computer_choice])

if user_choice == computer_choice:
    print("Draw")
else:
    if (user_choice == 0 and computer_choice == 1) or \
        (user_choice == 1 and computer_choice == 2) or \
        (user_choice == 2 and computer_choice == 0):
        print("You lose!")   
    else:   
        print("You win!")
