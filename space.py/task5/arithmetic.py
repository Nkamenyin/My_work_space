#!/usr/bin/python3

""" This an API that performs basic arithmetic operations (add, subtract, multiply, divide) using path parameters.
Example: /add/3/5 → 8"""

from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

@app.get("/calculate/{operation}/{num1}/{num2}")
def calculate(operation: str, num1: int, num2: int):

  try:
    if operation == "add":
      result = num1 + num2
    elif operation == "subtract":
      result = num1 - num2
    elif operation == "multiply":
      result = num1 * num2
    elif operation == "divide":
      if operand2 == 0:
        raise ZeroDivisionError("You can not divide by zero")
      result = num1 / num2
    else:
      raise ValueError("Invalid operation.")
    return {"result": result}
  except (ValueError, ZeroDivisionError) as e:
      raise HTTPException(status_code=400, detail=str(e))
