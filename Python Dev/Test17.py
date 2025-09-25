import math
import random

# Modules

# Here in this script we will be working on the python modules
# In python each python file(script) will be treated as a python module. We can import one file into another file and
# access the variables and functions and many more.

# To do that we will use import statement. Like import my_module

# Here I will mention some of the standard module we have in python.


'''
Random
'''
# This will be used to pick something randomly. Like below
import random
courses = ['Math', 'Art', 'History', 'Physics']
print(random.choice(courses))
# This will print random courses at each time.


'''
Math
'''
# This wil be used to do some mathematical operations
import math
rads = math.radians(90)  # Here I am getting the radians of 90 degrees
print(rads)
print(math.sin(rads))   # Printing the Sin value of that radians


'''
datetime
'''
# This will be used to do some date time operations.
import datetime
today = datetime.date.today()
datetime_of_today = datetime.datetime.today()
print(today)    # This will print the today's date
print(datetime_of_today)    # This will print today's the both date and time.

'''
calendar
'''

# This will be used to do some calendar operation.

import calendar
print(calendar.isleap(2017))    # This will print the False bcz 2017 is not a leap year
print(calendar.isleap(2020))    # This will print the True bcz 2020 is a leap year



''''
sys
'''
# This will be used to do system operations.
import sys
print(sys.path)     # This will print the current path of the script.
# Above statement will print multiple path locations which are Current Directory, Environmental path, site-packages.
# Let's say I have directory which is not in the project path (Desktop) and i need to add that to the path we can use
# the sys module like below.
sys.path.append("< Location of the Desktop >")  # This will add the desktop directory to tha Path.




'''
os
'''
# This will be ued to some operation on the operating systems.
import os
print(os.getcwd())  # This will print the current script's directory.
# If we want to see where this standard library is present in the system we can use the dunder file method( using two
#  underscores before and after the file. < __file__ > )
print(os.__file__)  # This will print the os.py file path.


'''
In python all the standard modules are nothing but python files which are automatically downloaded when we install
python.
So all the modules are in over system at some location when we import them that python file will be accessed.
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9
All the standard modules were there in the above mentioned location in my system. 
'''