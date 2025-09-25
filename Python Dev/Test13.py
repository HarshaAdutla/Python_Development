
# File Operations
# Write operations


"""
Here I am reading the lines from the text file, and then I am reversing those line, and then I am writing them in to
this file (testfile.txt).
Steps:
Open Text.txt file then read all lines
Reverse then
Write them to the testfile.txt file
"""
with open('Text.txt', 'r') as readfile1:        # Here w indicates that we are opening the file in read mode
    content = readfile1.readlines()     # This will store all the lines of readfile
    reversed(content)                   # Reversing the lines using reversed method
    # print(content)
    with open('testfile.txt', 'w') as writefile:        # Here w indicates that we are opening the file in write mode
        for line in reversed(content):              # Iterating through the list of reversed list
            writefile.write(line)               # Writing those values in the desired file
