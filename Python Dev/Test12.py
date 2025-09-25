# File Operations
# Read operations

# We have some data in Text.txt file, and now we are extracting the data from that file
"""
In File operations once we read the file up to like 5 lines in one place in the next step it will read the data from
6th line
"""
file = open('Text.txt')  # Here we are opening the Text file and creating an object to it (file)
print(file.read())  # It will read all the content of file.
# Output is :
# Viswamohan Reddy
# Harshavardhan Reddy
# Siva sudheer Reddy
# Pavan kumar Reddy
print(file.readline(2))  # It will read first two characters of the file
# Output is : Vi


file.close()

#  Here I am creating one more variable for the same file
file1 = open('Text.txt')
print(file1.readline())  # Here it will read and prints the first line in the file
# Output is : Viswamohan Reddy

print(file1.readline())
# Output is : Harshavardhan Reddy
# Here it will read and prints the second line in the file bcz first line is already read  in the 25th line
file1.close()

file2 = open('Text.txt')
# print(file2.readlines())
# Output is : ['Viswamohan Reddy\n', 'Harshavardhan Reddy\n', 'Siva sudheer Reddy\n', 'Pavan kumar Reddy\n']

# Here it printed all the data in a list by converting each line into a string
line = file2.readline()
while line != "":
    print(line)
    line = file2.readline()

file2.close()


# Here I am printing all lines
file3 = open('Text.txt')
for line in file3.readlines():
    print(" Final line are: " + line)
file3.close()

# Output is :
#   All line are: Viswamohan Reddy
#
#  All line are: Harshavardhan Reddy
#
#  All line are: Siva sudheer Reddy
#
#  All line are: Pavan kumar Reddy

"""
When we open a file make sure that we are closing the file after usage.
"""

"""
Usually in file operation when we open a file we need to write a to code to close the opened file,
but by using with open method we don't need to write a closing code.
"""

with open('Text.txt') as file4:
    print("I am using with open operation to print this line: " + file4.readline())

# Here when my cursor comes out of that block, it will treat it as file closed
# In the next script I am using with open method to do write operations