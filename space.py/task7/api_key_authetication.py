#!/usr/bin/python3

""" This API uses API keys for authentication. Generate and validate API keys to restrict access to certain endpoints."""

import uuid
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import APIKeyHeader

app = FastAPI()

api_keys = {}

# Function to generate a new API key
def generate_api_key():
    return str(uuid.uuid4())

# API Key Header
api_key_header = APIKeyHeader(name="X-API-Key")

# Dependency to validate API key
def get_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header not in api_keys:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key_header

# Endpoint to generate a new API key
@app.post("/generate_api_key")
def generate_key():
    new_key = generate_api_key()
    api_keys[new_key] = True
    return {"api_key": new_key}

# Protected endpoint
@app.get("/protected_data", dependencies=[Depends(get_api_key)])
def get_protected_data():
    return {"data": "This is protected data"}
