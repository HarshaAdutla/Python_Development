
# Finally Keyword

# We use finally block only when we use try and except mechanism
# This will run at the end no matter there is a failure or pass in our try except mechanism

try:
    with open('testingfile.txt', 'r') as file1:
        print(file1.read())
except Exception as e:
    print(e)
finally:
    print("finally block is executed")
"""
Here the file name that i mentioned in the line no 8 is not present in the system so except block executes then finally block executes
"""

try:
    with open('Text.txt', 'r') as file1:
        print(file1.read())
except Exception as e:
    print(e)
finally:
    print("try block executed and also finally block executed")

"""
Here we have the file so try will executes, even though try block finally will also executes
"""


"""
If my script has 50 lines of with a finally block, and if my script failed at 18th line then it will throws an error and
also it will execute finally block.
"""


# What is the purpose of using finally keyword everytime?
"""
-> Lets say after every test execution i need to clear the records, so at that time we will use finally keyword.

-> My test is created some records, so after test completed I need to clear all the created records so that time we will 
use finally keyword.

-> Let's say my test is created some data and then failed at some point, but when I re-run it will create data again and 
it will create some data issues if I didn't clear the old data, so no matter whether the test is passed or failed I need
to clearing the data after each execution.

Example: 
finally:
    print("Clear all records")

"""