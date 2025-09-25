
# Constructor:

"""
* Constructor is a method which is automatically called when we create an object for a class.
* If no constructor was defined then default constructor will be called.
* Even if we didn't create it in our class, at run time it will be created automatically and attached to that particular
class. We might not be able to see it our code.
"""

# Creating a constructor:
"""
* We need to provide two underscores at the start and end of the constructor(' __init__(self) ')
* Creating constructor is similar to method(function)
* Syntax to create constructor:
    def __init__(self):

* Here init is a keyword used to declare a constructor 
"""
class Caluculator:

    number = 200

    def __init__(self):
        print("*** This will be called automatically when an object is created for this class ***")
        """
        The above print method will be printed automatically when i create a object for this class.
        So when i run the class this print statement also printed in the output.
        """
    def firstMethod(self):
        print("It is a method in a class")

obj = Caluculator()
obj.firstMethod()
print(obj.number)


"""
There are two types of variables
1. Class variable
2. Instance variable

-> Class Variable : The variables which we define inside the class are called class variables ( In above number = 200 )
is a class variable.

-> Instance Variable :  The variables which we define inside a constructor are called instance variables.
 
"""


# Notes:
"""
* We can create n number of objects for a class, so the class variables are same for all objects.
* If we are sending any arguments in the object that many arguments has to be declared in constructor declaration, if it 
is not matched then it will throws an error. 
* We need to store those values in to the class as instance variables
Example: self.a = a
         self.b = b

"""

class Caluculator:

    number = 200

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("*** This will be called automatically when an object is created created for this class ***")
        """
        The above print method will be printed automatically when i create a object for this class.
        So when i run the class this print statement aslo printed in the output.
        """
    def firstMethod(self):
        print("It is a method in a class")

    def summetation(self):
         return self.firstNumber + self.secondNumber

obj = Caluculator(10, 20)
print(obj.summetation())



"""
* self keyword is mandatory for calling variable names in to methods.
* Instance and class variables have different purpose.
* Constructor name should be __init__ .
* new keyword is not required when you create an object (Not like in java).
"""