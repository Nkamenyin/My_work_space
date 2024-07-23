#!/usr/bin/python3

""" creating a password validator from functions a module created already.
The module is password_validator.py
This is done by importing the module"""

import password_validator
password = input("Enter Password: ")
if password_validator.validate_password(password):
    print("Valid password")
else:
    print("invalid password. Password must contain uppercase, lowercase, digits and special characters")
