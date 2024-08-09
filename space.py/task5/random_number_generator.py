#!/usr/bin/python3

""" An API that returns a random number between a given range provided as query parameters.
Example: /random?min=1&max=100 → 42"""

from fastapi import FastAPI, Query, Annotated
import random

app = FastAPI()

@app.get("/random")
def get_random_number(min: Annotated[int, Query()], max:Annotated[int, Query()]):
    random_number = random.randint(min, max)
    return {"random_number": random_number}
