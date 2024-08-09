#!/usr/bin/python3

"""Build an API with basic authentication. Allow users to register and log in, and use hashed passwords for security. Implement endpoints to protect certain resources that require authentication."""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext

# Define application instance
app = FastAPI()

# Password hashing context (using bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"])

# OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # Login URL changed

# User data model (for registration and login)
class User(BaseModel):
    username: str
    password: str

# Access token model (returned during login)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"  # Token type set to bearer

# Function to hash user password securely
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify user password against hashed version
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to retrieve user by username from storage (replace with database later)
def get_user(username: str) -> dict | None:
    return users.get(username)

# Function to authenticate user based on credentials
def authenticate_user(username: str, password: str) -> dict | None:
    user = get_user(username)
    if user and verify_password(password, user["password"]):
        return user
    return None

# User registration endpoint
@app.post("/register")
async def register_user(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    users[user.username] = {"username": user.username, "password": hash_password(user.username)}
    return {"message": "User created successfully"}

# User login endpoint (using form data)
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": user["username"], "token_type": "bearer"}

# Dependency to retrieve user based on provided access token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid access token")
    return user

# Protected route accessible only with a valid token
@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}!"}

# Public route accessible without authentication
@app.get("/public")
async def public_route():
    return {"message": "Hello, public user!"}
