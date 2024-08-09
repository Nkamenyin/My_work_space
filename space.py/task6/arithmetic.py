#!/usr/bin/python3

""" An API that performs basic arithmetic operations (addition, subtraction, multiplication, division). Use dependencies to manage and validate input parameters. """

from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()


def calculate(num1:float, num2:float, operation:str):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Can't divide by zero")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    return {"result": result}

@app.post("/calculate")
def calculate_handler(cal=Depends(calculate)):
    return cal
