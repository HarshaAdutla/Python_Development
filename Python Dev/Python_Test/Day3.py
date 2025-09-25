
'''
number = int(input("Enter any number: "))
if number % 2 == 0:
    print(f'{number} is even number.')
else:
    print(f'{number} is odd number.')
'''

'''
print(" ******* Pizza Order! *******")
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
# S == 15
# M == 20
# L == 25

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You types the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print("Total bill is: $", bill)

'''

''' ****** Treasure Map *****'''

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasureisland.")
print("Your Mission is to find the treasure.")
print("You are at a cross road which turn will you take.")
choice1 = input('You\'r at the cross road, where do you want to go? Type "Right" or "Left".\n').lower()
if choice1 == "left":
    choice2 = input("You've reached the lake. There is an island in the middle of the lake. "
                    "Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You've reached the island. There is a house with three doors Red, "
                        "Yellow and Blue. Which color door you want to choose.\n").lower()
        if choice3 == 'yellow':
            print("Congratulations. You found the treasure.")
        else:
            print("You have choose the wrong door. Game over.")
    else:
        print("You drowned in the lake. Game Over.")
else:
    print("You fell into a hole. Game Over.")


