'''
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = []
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


total = 0
for number in range(1, 101):
    total += number

print(total)

'''

import random

# Password Generator:-
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("*** Welcome to PyPassword Generator! ***")
nr_letters = int(input("How many LETTERS would you like in password? \n"))
nr_symbols = int(input("How many SYMBOLS would you like in password? \n"))
nr_numbers = int(input("How many NUMBERS would you like in password? \n"))
password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_symbols):
    password += str(random.choice(numbers))

print(password)
pass_list = list(password)
random.shuffle(pass_list)
password = ''.join(pass_list)
print(f'Your Password is: {password}')


