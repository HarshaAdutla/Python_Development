
# Tuples  AND  Dictionaries  AND Generators
"""
Tuples are similar to the list but immutable. ( Only two difference)
1. Tuples are immutable. Means once we declare the values in it, we can not do any modifications to the values.
2. Tuples will be enclosed with parenthesis ' () '
"""

values = (1, 2, 3, "String", 2.30)
print(type(values))      # Here checking the type
# Output is : <class 'tuple'>

# values[3] = "It is a String"    # Here i am trying to change the 3rd index value
# print(values)
# Output is : An error. Because tuples are immutable, we can't modify the data once we declare it.
# ______________________________________________________________________________________________________________________

# Dictionary
"""
Dictionaries will be define in flower brackets.
Dictionaries will have the data in ' key value pair '
"""

a = {1: "First Name", 2: "Second Name", "age": 25, "Name": "Harsh"}
# Here 1 is key and holds a value of ' First Name ' same for keys 2 and 3. If String is used no matter either key or -
# value quotes needs to be used
print(a["age"])     # Here printing the value using its KEY. There is no index identification in dictionaries.
# Output is : 25

print(a["Name"])
# Output is : Harsh

print(a[1])
# Output is : First Name

# ______________________________________________________________________________________________________________________

# How to create Dictionaries dynamically at Run time.

dict = {}
dict["First Name"] = "Harsh"        # This key value pair will be added to the dictionary
dict["Last Name"] = "Reddy"         # This key value pair will be added to the dictionary
dict["Gender"] = "Male"
print(dict)
# Output is : {'First Name': 'Harsh', 'Last Name': 'Reddy'}

# Now we can read the values as usual. One example shown below
print(dict["Last Name"])
# Output is : Reddy



''' ****************** Dictionaries ****************************** '''
print("****************** Dictionaries Comprehension ******************************")
# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Tony', 'Wade']
heroes = ['Batman', 'Superman', 'Spider man', 'Iron man', 'Deadpool']
superheros = list(zip(names, heroes))
print("Zipped Super Heroes:", superheros)
# Above zip will print the list of tuples.
# It will match the items as 1st index in first list will be matched with 1st index in the second list.
# We need to convert this to list(as above).

my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print("Super Heroes Dictionary is:-", my_dict)      # This will print the name and hero as key value pair.

# Both above two methods are fine.
# Comprehensive way to achieve the same is
my_dict = {name: hero for name, hero in zip(names, heroes)}
print("Comprehensive dictionary for superheroes is:-", my_dict)

# Now I am doing the same thing but I kept one condition is name is Peter then it should not append to the dict.
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print("Conditioned dictionary for superheroes is:-", my_dict)
# This won't add the peter to and spider man to the dict.



''' ****************** Sets ****************************** '''
print("****************** Sets Comprehension ******************************")
# Set: Set is similar to the list, but it will have all the unique values only not the duplicate values(repeated values)
nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 4, 6, 7, 8, 7, 8, 9, 7, 9, 10, 10]
# This is a list but when we make this as a set all the repeated values will be removed.

my_set = set()
for num in nums:
    my_set.add(num)
print("Set is:-", my_set)
# Comprehensive way to do the same is
my_set = {n for n in nums}
print(my_set)
# For this we use curly braces only, but we don't use key value pairs.
# This is printing a dict of numbers, need to check.

# We can perform the other operation as we did for list

''' ****************** Sets ****************************** '''
print("****************** Generator Expressions ******************************")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_gen(nums):
    for num in nums:
        yield num*num
my_gen = my_gen(nums)
for i in my_gen:
    print(i)

# The comprehensive way to do the same is
# Here we dont use brackets or curly braces we use parenthesis
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
