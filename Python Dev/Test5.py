# For loop

values = [1, 2, 3, 4, 5, 6, 7]

for i in values:
    i = str(i)
    print("Values is:" + i)
    if i == "5":
        print("Met the value 5 here.")

# Here I am trying to print the list values with multiple of 2

values = [1, 2, 3, 4, 5, 6, 7]

for i in values:
    j = i*2
    # print(i*2)    # This also prints the values with multiple of 2.
    multiple = str(j)
    print("Values after multiplication is:" + multiple)
# ______________________________________________________________________________________________________________________

# Sum of the First five natural Numbers (1+2+3+4+5 = 15)
summation = 0
for j in range(1, 6):   # If the range is (i, j), then it will iterate it from i to j-1. I.e., it iterates 1 to 5.
    # print(j)    # Printed th natural numbers.
    summation = summation + j
    print(summation)
# It will print that current sum of each iteration. We need to keep the print function outside the for loop.
summation = str(summation)
print("Sum of first five natural numbers is:" + summation)
# We cannot concatenate the string with integer, so in the above step, I have changed it to string
# Output is: Sum of the first five natural numbers is:15

# ______________________________________________________________________________________________________________________


# Here I am printing the numbers with index difference
print("********")       # Just to Make the difference in the output
for i in range(1, 10, 2):   # Here 2 in the range box is the difference box (In jav we mention diff as i++).
    print(i)        # In above, it prints values from 1 to 9(limit is 10) with 2 index differences.

# In other programming languages like java, we write a condition like (i=0,i<5,i+2) means we need to add 2 in each
#  iteration, but in python we will write that as third argument as I did in the above.
# Output is:
# 1
# 3
# 5
# 7
# 9

# Here we are not providing the initial value by default it will treat 0 as initial value.
print("****SKIPPING THE INITIAL VALUE****")
for i in range(10):     # It will print all natural numbers up to 9 starting to 0
    print(i)
