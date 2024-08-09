#!/usr/bin/python3

"""An API that assigns roles to users (e.g., admin, user) and restricts access to certain endpoints based on user roles."""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
import jwt
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Role(Enum):
    USER = "user"
    ADMIN = "admin"

class User(BaseModel):
    username: str
    email: str
    password: str
    role: Role = Role.USER

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"role": data["user"].role.value})
    secret_key = os.getenv('SECRET_KEY')  # Access secret key from environment
    return jwt.encode(to_encode, secret_key, algorithm="HS256")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        secret_key = os.getenv('SECRET_KEY')  # Access secret key from environment
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        username = payload.get("username")
        role = Role(payload.get("role"))
        user = User(username=username, role=role)
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@app.get("/users/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/admin/data")
def get_admin_data(current_user: User = Depends(get_current_user)):
    if current_user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden, Only admins can access this data")
    return {"data": "admin data"}
