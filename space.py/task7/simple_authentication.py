#!/usr/bin/python3

""" This API handles basic authentication. It allows users to register and log in, and use hashed passwords for security. Implement endpoints to protect certain resources that require authentication."""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Optional

app = FastAPI()

users = {}

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_user(username: str):
    return users.get(username)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user["password"]):
        return False
    return user

@app.post("/register")
def register(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    users[user.username] = {"username": user.username, "password": hash_password(user.password)}
    return {"message": "User created"}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": user["username"], "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

@app.get("/secured")
def secured_route(user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {user['username']}!"}
