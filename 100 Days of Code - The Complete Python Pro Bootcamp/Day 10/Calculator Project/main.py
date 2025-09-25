def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

import art



mathematical_operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": division
}

def calculator():
    print(art.logo)
    action = True
    number1 = float(input("What is the first number?: "))
    while action:
        for symbol in mathematical_operations:
            print(symbol)
        operation = input("Pick an Operation: ")
        number2 = float(input("What is the next number?: "))
        answer = mathematical_operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {answer}")

        continue_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
        if continue_operation == "y":
            number1 = answer
        else:
            action = False
            print("\n" * 40)
            calculator()

calculator()















