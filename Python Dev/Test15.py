# Try catch Mechanism

# If we know that some test is going to fail, but we don't want to stop the execution then we use try exception blocks

try:
    # with open('Text.txt', 'r') as file:
    with open('testing.txt', 'r') as file:  # Here this doesn't exist in the system so it should have thrown an error
        file.read()
except:
    print("Reached the exception block")
    # Output is : Reached the exception block


# But we are using try and except block so if we face issues in try block it won't fail the print it will execute
# the except block

"""
In 6th line I have given a valid file name so try block will executes without any error so controller won't go inside 
of the except block.

Controller will goes only except block when if fails in try block
"""

"""
In line number 10 I am printing my custom message but if I want to print the error message in the console then 
"""


try:
    with open('testingfile.txt', 'r') as file1:
        print(file1.read())
except Exception as e:
    print(e)

# Output is : [Errno 2] No such file or directory: 'testingfile.txt'

"""
Check in the console that test passed successfully even though it has an error bcz except block is catching that error 
and we are printing the error message in the console.
"""
