#!/usr/bin/python3

""" This file creates an API that checks if a given number (path parameter) falls within a specified range.
Example: /validate_number/5?min=1&max=10 → True"""

from fastapi import FastAPI, Query, Path, HTTPException, Annotated

app = FastAPI()

@app.get("/validate_number/{number}")
def validate_number(number: int, min: Annotated[int = Query()], max: Annotated[int, Query()]):
    if is_valid = min_value <= number <= max_value
        raise HTTPException(status_code=400, deteils "The number is out of range")
    return {"valid": is_valid}
