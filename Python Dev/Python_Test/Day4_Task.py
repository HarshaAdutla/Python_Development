'''
Rock Paper Scissor game with computer
'''


import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


'''
options = [Rock, Paper, Scissor]
system_choice = random.choice(options)

choice = int(input("What do you choose? 0 for Rock , 1 for Paper and 2 for Scissors.\n"))

if choice <= 3:
    your_choice = options[choice]
    print("Your Choice:", your_choice)
    if your_choice == system_choice:
        print(f"System Choice:\n", system_choice, "\nIt's Draw")
    if your_choice != system_choice:
        if your_choice == options[0] and system_choice == options[1]:
            print(f"System Choice {system_choice} You Lose")
        elif your_choice == options[0] and system_choice == options[2]:
            print(f"System choice {system_choice} YOU WIN\n Rock Wins Scissor")
        elif your_choice == options[1] and system_choice == options[0]:
            print(f"System Choice {system_choice} YOU WIN\n Paper Wins Rock")
        elif your_choice == options[1] and system_choice == options[2]:
            print(f"System choice {system_choice} You Lose")
        elif your_choice == options[2] and system_choice == options[0]:
            print(f"System choice {system_choice} You Lose")
        elif your_choice == options[2] and system_choice == options[1]:
            print(f"System choice {system_choice} YOU WIN\n Scissor Wins Paper")
else:
    print("Select valid input number.")

'''
game_images = [Rock, Paper, Scissor]
user_choice = int(input("What d oyou choose? 0 for Rock or  1 for Paper or 2 for scissor.\n"))
computer_choice = random.randint(1, 2)

if user_choice >= 0 and user_choice <=2:
    print("Your Choice:", game_images[user_choice])

print("Computer Choice:", game_images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("You selected invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice == computer_choice:
    print("It's Draw")
