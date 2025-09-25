

""" ****************** List Sorting ****************************** """
from Test3 import names

print("****************** List Sorting ******************************")

# Here we will be sorting the lists, dictionaries and tuples.
li = [2, 6, 4, 7, 1, 3, 8, 5, 9]
s_li = sorted(li)
print("Sorted list is:-", s_li)
print("Original List is:-", li)

# Above original is not sorted bcz we used sorted method that's why we set it to a new variable.
# sorted will create a new list
li.sort()
print("Original Sorted list:-", li)
# sort() sort function will sort the original list and returns None.
s_li = li.sort()
print(s_li)     # Output is: None
# If we use the sort() method by setting a variable it will return None

# To sort in the Descending order
# Using sorted() function:-
s_li = sorted(li, reverse=True)
print("Reversed list:-", s_li)
# Using sort() method:-
li.sort(reverse=True)
print(li)


# Sorted() method has more flexibility then the sort() bcz we can pass any iterable.
tup = (9, 7, 8, 5, 6, 3, 5, 4, 2, 1)
# tup.sort()        # This will through an error so we can use the sorted function.
# print(tup)
s_tup = sorted(tup)     # This will sort the values and converts to a list.
# s_tup = sorted(tup, reverse=True)       # Same way we can do the reverse operation too.
print("Sorted tuple is:-\t", s_tup)


""" ****************** Dictionaries Sorting ****************************** """
print("****************** Dictionaries Sorting ******************************")
my_dict = {'name': 'Harsha', 'job':'programming', 'age': 28}
# my_dict.sort()      # This will through an error.
my_dict1 = sorted(my_dict)      # This will print the all sortd key values.
print("Sorted Dictionary is:-\t", my_dict1)


print("****************** Sorting Numbers ******************************")

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)
# Now I want to sort them based on the absolute values. We use key parameter.
s_li = sorted(li, key=abs)
print(s_li)     # Output is: [1, 2, 3, -4, -5, -6]



class Employee():

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Harsha', 28, 10000)
e2 = Employee('Siva', 30, 20000)
e3 = Employee('Viswa', 29, 40000)

employees = [e1, e2, e3]
# s_employees = sorted(employees)   # This will through a Type Error. Bcz it doesn't know on which value sort has to do.
# So we need to mention on which value we need to perform the sorting.

def e_sort(emp):
    return emp.age
s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

# The above e_sort function will take the emp name and in the s_employee line we are using e_sort method.
# If i want to do sorting on emp age we need to change the age in e_sort function.
# We can use the reverse key also.

# We can use the lambda function to do sort operation.
'''
s_employees = sorted(employees, key=lambda e: e.name)

If we use the lambda function, then def e_sort function is not needed bcz we are sorting on name in the lambda operation
itself.
'''
















