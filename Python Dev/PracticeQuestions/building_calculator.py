# Here I am building a normal calculator functionality. Like we see in the general stores.

# Question:- Write a python program to add the inputted numbers and end the process when 'q' is entered.

total = 0

while(True):
    user_input = input("Enter the Item Price, Or Press q to quit. \n")
    if user_input!= "q":
        total = int(user_input) + total
        print(f"Your total bill so far : {total}.")
    else:
        print(f"Your Total Bill is: {total}.\nThank You For Shopping With Us.")
        break

