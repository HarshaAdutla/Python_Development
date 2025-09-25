
print(type(1234))
print(type("Hello"))
print(type(3.1459))
print(type(True))


# print("Number of letters in your name: " + str(len(input("Enter your name:"))))

print(3 * (3 + 3) / 3 - 3)


# Tip Caluculator

print("Welcome to the Tip caluculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))
tip_amount = tip_percentage/100 * total_bill
total_amount = (tip_amount + total_bill) / num_of_people

payable_amount = round(total_amount, 2)
print(f"Each person should pay ${payable_amount}")