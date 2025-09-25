
# Inheritance

# Acquiring properties of parent class
"""
Inheritance means using parent file classes and methods in a child file

"""
from Test9 import Caluculator


class TestDemo(Caluculator):
    number2 = 200

    def __init__(self):
        Caluculator.__init__(self, 3, 5)

    def firstFunction(self):
        return self.number2 + self.firstNumber + self.number    # Here firstNumber and number are parent class variables

obj1 = TestDemo()
print(obj1.firstFunction())





"""
Here I have added a class which we defined in previous script(Test9). So now I can use all methods that I defined in
previous script(Test9)
"""
"""
When we inherit code from parent class we need to create relation between constructor too.
If parent class has a default constructor then no need to create anything but we declare any constructor in parent class
then we need to create the constructor in child class as well
"""