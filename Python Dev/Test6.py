
# While loop

a = 4
while a > 1:
    if a != 3:      # Here I am trying not to print the number 3. Once it equals to 3 it won't go in so print won't work
        print(a)
    a = a - 1
print("While loop execution is completed")

# ______________________________________________________________________________________________________________________

# Break condition
a = 4
while a > 1:
    if a == 3:
        break       # Here if 3 is there then the while loop will be halted. Once it meets the condition it will stop
                    # the loop excution.
    print(a)
    a = a - 1
print("While loop execution is completed")
# Output is :
# 4
# While loop execution is completed

"""
In above, it started with four so 4 is printed then the value becomes 3 and it matches the condition so if loop executed
and in the if loop break was there so it will comes out of the while loop
"""

# ______________________________________________________________________________________________________________________

# Continue condition

print("**************")
k = 10
while k > 1:
    if k == 9:      # Here when condition marches then it will skip that iteration and continues to next iteration.
                    # Here it won't print the value 9
        k = k - 1
        continue        # It reaches here and skips that iteration and continue to next iteration
    if k == 3:
        break
    print(k)
    k = k - 1
print("While loop execution is completed")
