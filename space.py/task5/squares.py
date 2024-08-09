#!/usr/bin/python3

"""This is an API that returns the square of a number provided as a path parameter.
Example: /square/4 → 16"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/square/{number}")
def get_square(number: int):
    return {"Result": number * number}
