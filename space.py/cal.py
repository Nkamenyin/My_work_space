#!/usr/bin/python3

""" creating a simple calculator that handles +,-,/,*.
Using calculator.py as my module"""

import calculator
a = float(input("Enter number: "))
operator = input("Carry out operation: ")
b = float(input("Enter number: "))

try:
    result = calculator.cal(a,operator,b)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
