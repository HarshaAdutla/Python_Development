import random

random_number = random.randint(1, 10)
print(random_number)

'''
In above I have imported random module so we can get some random values. This random module has multiple functions 
in it. Which are randint, random and uniform, etc,.

randint:- randint requires two ranges which will generate the random numbers within the range including both the 
numbers. Which means it will include both initial value and also the ending value(not like the index).
( a <= X <= b )

'''
# randint:-

randint_number = random.randint(1, 10)
print("Randint Numbers is: ", randint_number)
'''
This will print any number starting from 1 to ending 10. 
'''

'''
* random:- random is another function in random which is mostly used function. It will generate numbers starting 
from 0.0 to 1 but it excludes the 1. ( 0.0 <= X < 1.0 )

* Which means it will print floating numbers stating from 0.0000----1 to ending at 0.9999---9 but it will never print 1.0.
* It always prints float starting from 0. only to convert it into integer we need to multiply it with 10.
'''
random_number = random.random()
print("Random Number is:", random_number)       # Output like this: 0.1468928896552404
random_number2 = random.random() * 10
print("Random Number2 is:", random_number2)     # Output like this: 4.009943480696317

# If we want two-digit numbers the nwe can multiply it with two digits (100)
two_digit_number2 = random.random() * 100
print("Two Digit Random Number2 is:", two_digit_number2)       # Output like this: 49.83875498033312


'''
uniform:- uniform is another function in the random module. It is almost same as random but it will include both 
initial value and ending value. But there is very less chance of getting the ending value bcz it will return the floats.
( a <= X <= b )
random.uniform(1, 10)
it will print 1 with floating values(1.0868798--). And less chance of printing 10 bcz it has to print the 
float(10.0000000--0) because the condition is <= so if it is 10.00001 also it won't satisfy the condition. 
'''

random_float = random.uniform(1, 10)
print("Random Float Number is:", random_float)      # Output like this: 9.49710216714151



'''
Challenge:- We need to print Heads and Tails using random module. 
'''

number = round(random.random())     # I have used round of to get the value 1
if number == 1:
    print("Heads")
else:
    print("Tails")
# In above, I have used random function and used the round of method. We can do this with randint as well(randint(0, 1))

'''
Choice:- It will choose one item from the list. Below I have written an example cof choosing a person name.
Fun:- Who's name come will have to pay the bill.😂
'''
# Option 1:-
names = ["Viswa", "Harsha", "Siva", "Pavan", "Shanmuk"]
print(random.choice(names))
# Option 2:-
person_number = random.randint(0, len(names)-1)     # To get the index i have used function.
print(names[person_number])
