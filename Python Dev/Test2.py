
# Lists  AND List Comprehensions
"""
List data type is not mutable. Means We can modify the list values again if we want to.
Tuples are mutable. Means once we declare the values in it, we can't do any modification to the values.
List will be enclosed with square brackets ' [] '
"""


values = [1, 2, "It is a String", 2.31]
print(values)
# List is a data type that allows multiple values and can be different data types
print(values[0])        # index will start from 0 in lists
# Output is : 1

print(values[-1])       # It will print the last value in the list
# Output is : 2.31

print(values[1:3])      # It will start printing values from index 1 to index 3.
# Output is : [2, 'It is a String']

values.insert(3, "Hello")   # Here we can add values to list using insert operation, It will be added in 3rd index
print(values)
# Output is : [1, 2, 'It is a String', 'Hello', 2.31]

values.append("End value")     # Here append will add the value at the last in the list
print(values)
# Output is : [1, 2, 'It is a String', 'Hello', 2.31, 'End value']

values[2] = "Updated String"    # Here we are updating the second value so previous value wil be overwritten
print(values)
# Output is : [1, 2, 'Updated String', 'Hello', 2.31, 'End value']

del values[1]       # Here it will delete the first index value ( 2 is removed from the list)
print(values)
# Output is : [1, 'Updated String', 'Hello', 2.31, 'End value']



# If we want to know how many values were there in any list we can use length function
print(len(values))
# Output is : 5

''' Returning the last value in the list '''
# 1
# Here I have called the last item in the list using index
total_values = len(values)
required_item = total_values - 1
print(values[required_item])
# Output is : End Value

# 2
# I have optimized the above 3 lines of code to a single line
print(values[len(values)-1])
# Output is : End Value

# 3 - Easy Way
# It is versy Easy to use -1 to get the last item.
print(values[-1])
# Output is : End Value


'''
List Comprehensions
'''

# Will perform some of the list operation in comprehensive way.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# This will add all numbers in the nums to my_list.
# The comprehensive way to do the same operation is
my_list1 = [n for n in nums]
print("My_list1 is:-", my_list1)

# To perform Square and more is
my_list1 = [n*n for n in nums]
print("Squared List is:-", my_list1)


''' ************************************************ '''
# We can do the same by using lambda function

my_list1 = map(lambda n: n*n, nums)
# print("Lambda squared list is:-", my_list1)     # It will print memory location

# But in my system it is ot working, just printing the memory location.
# Above filter returns an iterator not a list so when print the my_list2 directly it will print the memory location.
# We need to convert that to list first. Like below
my_list1 = list(my_list1)
print("Lambda list is:-", my_list1)



''' ************************************************ '''
# For Qube
my_list1 = [n*n*n for n in nums]
print("Qubed List is:-", my_list1)


''' ************************************************ '''
# Lets I have to verify if the number is even then only I have to add it to the list.
my_list2 = []
for n in nums:
    if n % 2 == 0:
        my_list2.append(n)
print("Even Numbered List:-", my_list2)
# To do the same in comprehensive way

my_list2 = [n for n in nums if n % 2 == 0]
print("Comprehensive Even numbered List:-", my_list2)


''' ************************************************ '''
# We can do the same using lambda functions also but in my system it is not working

my_list2 = filter(lambda n: n % 2 == 0, nums)
# print("Lambda list is:-", my_list2)       # It will print memory location
my_list2 = list(my_list2)
print("Lambda list is:-", my_list2)

# Above filter returns an iterator not a list so when print the my_list2 directly it will print the memory location.
# We need to convert that to list first.

# We can perform the nested for loop and create a combination of tuple

''' ************************************************ '''
# Ques:- I want a (letter, number) pair for each letter in 'abcd' and each number in '0123'.
# Ams:-

my_list3 = []
for letter in 'abcd':
    for number in range(4):
        my_list3.append((letter, number))
print("Combination list is:-", my_list3)

# List comprehension for the same is
my_list3 = [(letter, number) for letter in 'abcd' for number in range(4)]
print("Comprehensive list3 is:-", my_list3)