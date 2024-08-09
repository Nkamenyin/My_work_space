#!/usr/bin/python3

""" This API calculates simple interest based on principal, rate, and time provided in the request body.
Example: POST /interest with request body { "principal": 1000, "rate": 5, "time": 2 }"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for interest input
class Simple_interest(BaseModel):
    principal: float
    rate: float
    time: float

@app.post("/interest")
def calculate_interest(input: Simple_interest):
    interest = (input.principal * input.rate * input.time) / 100
    return {"Simple interest": interest}
