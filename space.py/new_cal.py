#!/usr/bin/python3

"""A basic calculator program to handle exceptions such as division by zero, invalid input types (like strings instead of numbers), and unsupported operations"""

def cal(a, operator, b):
    try:
    # Check for division by zero
        if operator == "/" and b == 0:
            raise ZeroDivisionError("You can not do division by zero")

    # Perform calculation based on operator
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        else:
            raise ValueError("Unsupported operation: " + operator)
    except (TypeError, ValueError) as e:
            return "Invalid input: " + str(e)

#basic calculation
a = float(input("number: "))
operator = input("Carry out operation: ")
b = float(input("number: "))
result = cal(a, operator, b)
print(f"{result}")
