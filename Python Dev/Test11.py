
# Advanced Operations on Strings, Dictionaries, List, Numbers

str = "Harshavardhan Reddy"     # This is an Example string

print(str[1])       # Extracting characters using index
# Output is : a

print(str[0:6])     # Printing a substring using from and to indexes
# Output is : Harsha


# We can not concatenate a string with an integer
# To concatenate a string and integer we can use the formate method like below

name = "Harsha"
age = 26

statement = "{} {}".format(name, age)   # We are concatenating the string and integer and storing it in a variable
print("Statement is : " + statement)
# Output is : Statement is : Harsha 26


# We can concatenate two strings directly
str1 = "Harshavardhan "
str2 = "Reddy"

name = str1 + str2

print(name)
# Output is : Harshavardhan Reddy


# Checking the substring

stringOne = "Harshavardhan Reddy"
stringTwo = "Reddy"

print(stringTwo in stringOne)       # line 39 and 40 both works
print(stringOne.__contains__(stringTwo))    # These two line (39 & 40) will print true or false as result
# Output is : True


# Split (Splitting a string)

email = "harsha.adutla@gmail.com"
# Here I am trying to split the above string based on the dot ' . '
var = email.split(".")
print(var)    # This will separate the sting and gives out put in a list
# Output is : ['harsha', 'adutla@gmail', 'com']

# If I want first value in the list I will print it using index
print(var[0])
# Output is : harsha



# Trim
"""
Trim is used to remove the white spaces in the beginning and ending (leading and trailing) of a string.
In python we can not directly use trim, we need to use one method which is strip.
"""
stringThree = "   It is Great    "
value = stringThree.strip()
print("Values before trim is :" + stringThree)  # Output is : Values before trim is :   It is Great
print("Value after trim is: " + value)
# Output is : Value after trim is: It is Great


# If we want to remove only the beginning white spaces not the ending white spaces then we need to lstrip( leftstrip)
print(stringThree.lstrip())
# Output is : It is Great

# Similarly if we want to remove the ending white spaces then we need to use rstrip (rightstrip)
print(stringThree.rstrip())
# Output is :  It is Great
''' White space at the beginning is still there.'''

# We can upper case and lower case of the strings like below
message = "Hello World"
print(message.lower())
# Output is : hello world
''' This will change all the letters in to lower case letters.'''


print(message.upper())
# Output is: HELLO WORLD
''' This will change all the letters in to upper case letters.'''


# By using length method we can check how many characters were there in a string
print(len(message))
# Output is : 11
'''It prints the number not the string.'''


# If we want check how many times a character or a word repeated in a string we can use the count method
print(message.count('l'))
# Output is : 3
''' Bcz 'l' was repeated 3 times in the string.'''

# Here I am checking for a word in a string
message1 = "Hello World Hello"
print(message1.count("Hello"))
# Output is : 2
''' Bcz Hello was repeated two times in the string.'''


# If we want to find any character in the string we can use find method like below
print(message.find('World'))    #
# Output is : 6
''' If the character or word present in the string then it will print their starting index in the output.'''


print(message.find("Namaste"))
# Output is : -1
''' If the character or word not preset in the string it will print -1 in the output'''



# We can replace any characters or words in the string using replace method
message.replace("World", "Universe")
print(message)
# Output is : Hello World
''' So here replace method will take two arguments first one will be the word which we want to replace and another
 one will be the word that we want to replace it with.
 
 But we we run this it won't print "Hello Universe" bcz replacement was not happened properly, to make it properly
 we need store it in a new or same variable. Like below'''
message = message.replace("World", "Universe")
print(message)
# Output is : Hello Universe



print("*** String Formatting ***")
# Concatenating two strings
greeting = "Namaste"
name = "Harsha"
greeting_Note = greeting + "," + name
print(greeting_Note)
# Output is : Namaste,Harsha
''' In this way we can concatenate the strings. We can do this using format method(best use)'''



greeting_message = "{},{}. Welcome".format(greeting, name)
print(greeting_message)
# Output is : Namaste,Harsha. Welcome



# Again we can format it more easy way like below
# These are called fstrings
greeting_message = f"{greeting},{name}.Welcome"
print(greeting_message)
# Output is : Namaste,Harsha. Welcome
''' It prints the same output. There are called fstrings.'''


''' These fstrings are better for any other operations too. Like below'''
greeting_message = f"{greeting},{name.upper()}.Welcome"     # Changed the name to upper case
print(greeting_message)
# Output is : Namaste,HARSHA.Welcome


'''
We have a dir function which will give us all the possible attributes which we cna perform on that variable. Like below
'''
print(dir(message))
# Output is :
''' ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 
'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill']'''
# We cna perform these many operations on that particular variable. And if want know about any of these methods we can
# use help function like below.
print(help(str))


print("*** String Formatting ***")

# We can format string in different ways with different data. Like Below

person = {'name': 'Harsha', 'age': 28}

sentence = 'My name is {}, and I am {} years old'.format(person['name'], person['age'])
print(sentence)
# Output is : My name is Harsha, and I am 28 years old


# If we want to we can explicitly number the placeholders. Like Below
sentence = 'My name is {0}, and I am {1} years old'.format(person['name'], person['age'])
print(sentence)
# Output is : My name is Harsha, and I am 28 years old

# By explicitly numbering we can use same strings again and again (Above example also works)
tag = "Hi"
text = "Namaste"

mess = '<{0}><{1}><{0}'.format(tag, text)
print('message is : ' + mess)
# Output is : message is : <Hi><Namaste><Hi

# In above examples we are passing the dictionary values in the arguments, we can pass them within the placeholders.
person = {'name': 'Harsha', 'age': 28}

sentence = 'My name is {0[name]}, and I am {1[age]} years old'.format(person, person)
print(sentence)
# Output is : My name is Harsha, and I am 28 years old

'''
In above while passing we mentioned two placeholders that's why we passed two arguments in to the format method.
We can do this by passing only one argument. Like below.
'''
person = {'name': 'Harsha', 'age': 28}

sentence = 'My name is {0[name]}, and I am {0[age]} years old'.format(person)
print(sentence)
# Output is : My name is Harsha, and I am 28 years old

'''
Here I have just changed the number in the placeholder to 0 that's why I have passed only one argument to the format
method.
'''



'''
Now here I am going to create a class and pass arguments when creating the instance of that class
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Person('Harsha', '28')
message = 'My name is {0.name}, and I am {0.age} years old as of today.'.format(obj)
print(message)
# Output is : My name is Harsha, and I am 28 years old as of today.



# We can also send keyword arguments to the format. Like below
sentence = 'My name is {name}, and I am {age} years old'.format(name='Harsha', age='28')
print(sentence)
# Output is : My name is Harsha, and I am 28 years old

# We can pass the keyword arguments to the format in another way also
person = {'name': 'Harsh', 'age': '23'}
sentence = 'My name is {name}, and I am {age} years old *'.format(**person)
print(sentence)
# Output is : My name is Harsh, and I am 23 years old *



# Numbers
print('**** Numbers ')

# We have some defined methods to work with numbers.
# If we want to print the absolute value of any negative number we can use the abs (absolute) method. Like below
num = -3
print(abs(num))
# Output is : 3

# Round

print(round(3.75))
# Output is : 4

# We can also pass a second argument to round function that tells how many digits that we want to round to
print(round(3.7568, 2))
# Output is : 3.76      Bcz 3.7568 is near to 3.76


# Arithmetic Operations

# Addition
print(4 + 2)        # 4 + 2     // 6

# Subtraction
print(4 - 2)        # 4 - 2     // 2

# Multiplication
print(4 * 2)        # 4 * 2     // 8

# Division
print(4 / 2)        # 4 / 2     // 2

# Floor Division
print(4 // 2)       # 4 // 2    // 0  Bcz prints the reminder
print(5 // 2)       # 5 // 2    // 2


# Exponent
print(4 ** 2)       # 4 ** 2    // 16


# Modules
print(4 % 2)        # 4 % 2     // 0
print(5 % 2)        # 5 % 2     // 1



# Comparisons:
# Equal:
# Not Equal:
# Greater Than:
# Less Than:
# Greater or Equal:
# Lesser or Equal:

num1 = 2
num2 = 3
print(num1 == num2)
# Output is : False     Bcz both numbers are not equal
print(num1 != num2)
# Out put is : True     Bcz Both are not equal
print(num1 > num2)
# Out put is : False    Bcz 2 is not greater than 3
print(num1 < num2)
# Output is : True      Bcz 2 is less than 3
print(num1 >= num2)
# Output is : False     Bcz 2 is not greater or equal to 3
print(num1 <= num2)
# Output is : True      Bcz 2 is less than or equal to 3 ( less)


# If any integer is in the string then we can cast that to inter by changing the type

num1 = '1001'
print(type(num1))
print(num1)
num1 = int(num1)
print(type(num1))
print(num1)