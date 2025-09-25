
#  Variables have two different scopes, 1. Local Scope and 2. Global Scope.

number = 1

def my_function():
    number = 2
    print(f"Local Scope: {number}")

my_function()
print(f"Global Scope: {number}")



#  In above example number = 2 is inside the function so the scope of that variable is only to that function only.
#  And number = 1 is on the outside of the function the scope of the variable is outside the function.
#  When we run the above program variable with same name defined in two different places. One is local and another is
#  global. If we try to call that variable outside function it will print outside value but if we call it inside then
#  the inside value will be printed.
#  So the Output will be Local Scope will be printed first and then Global Scope value will be printed.

