#!/usr/bin/python3

"""This API that uses JSON Web Tokens (JWT) for user authentication. Implement login and protected endpoints, ensuring only authenticated users can access certain resources."""

from fastapi import FastAPI, HTTPException, APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, Token, OAuth2PasswordRequestForm
import time
import jwt
from passlib.context import CryptContext
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    hashed_password:str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# access token with payload and expiration time
def create_access_token(data: dict, expires_in: int = 3600):
    to_encode = data.copy()
    expire = time.time() + expires_in
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "your_secret_key", algorithm="HS256")
    return encoded_jwt

# verify access token
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, "your_secret_key", algorithms=["HS256"])
        username = payload.get("username")
        if not username:
            raise credentials_exception
        return {"username": username}
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception

def get_user(username: str):
    users = {
        "user1": User(username="user1", email="user1@example.com", hashed_password=pwd_context.hash("password1")),
        "user2": User(username="user2", email="user2@example.com", hashed_password=pwd_context.hash("password2")),
    }
    return users.get(username)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Create an APIRouter for authentication endpoints
router = APIRouter(prefix="/auth", tags=["Authentication"])

# Login endpoint to generate access token upon successful authentication
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"},)
    try:
        user_data = verify_token(token, credentials_exception)
        return user_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {e}")

@app.get("/users/me")
def read_current_user(current_user: dict = Depends(get_current_user)):
