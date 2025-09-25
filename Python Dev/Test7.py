# Functions

# Function is group of related statements that perform a specific task
# Function name should be defined with ' def ' i.e def functionName():

print("*** Printing the message by calling function ***")
def greetMe():  # Function declaration
    print("Namaste")
greetMe()       # Function call
# Output is : Namaste


# ______________________________________________________________________________________________________________________

# Sending Parameters to the function
print("*** Sending one parameter to the function at the function call time ***")  # Just to separate the output
def greetMe(name):  # Function declaration
    print("Namaste " + name)
greetMe("Harshavardhan Reddy")  # Added one parameter to the function at the run Function call time.
# Output is : Namaste Harshavardhan Reddy


# ______________________________________________________________________________________________________________________

print("*** Sending two parameters to the function at the function call time ***")
def addNumbers(a, b):  # Sending two parameters to a function
    print(a + b)
addNumbers(10, 20)
# Output is : 30


# ______________________________________________________________________________________________________________________

print("*** Running Two Functions at a Time ***")

def greetMe(name):
    print("Namaste " + name)

def addNumbers(a, b):
    print(a + b)

greetMe("Harshavardhan Reddy")
addNumbers(10, 12)
# Output is :
# Namaste harshavardhan Reddy
# 22

"""
In above, I have called two functions at a time.
"""


# ______________________________________________________________________________________________________________________

# Here instead of printing, I am returning the output to the function itself

print("*** Returning the output to the Function itself ***")

def greetMe(name):
    return "Namaste " + name

def addNumbers(a, b):
    return a + b

print(greetMe("Harshavardhan Reddy"))
print(addNumbers(15, 42))