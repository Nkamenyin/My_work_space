#!/usr/bin/python3

"""A basic login system that checks username and password against a stored list. Handle exceptions for invalid input, and locked accounts after multiple failed attempts"""

#user deteils
users = {
        "user1": {"password": "pass1", "attempts": 0, "locked": False}
        }
import time

def login(username, password):
    try:
        user = users[username]
        if user["locked"]:
            raise ValueError("Account locked. Try again later.")
        if user["password"] != password:
            user["attempts"] += 1
            if user["attempts"] >= 3:
                user["locked"] = True
                raise ValueError("Account locked. Try again later.")
            raise ValueError("Invalid password. Try again.")
        # Reset attempt count on successful login
        user["attempts"] = 0
        return True
    except KeyError:
        raise ValueError("Invalid username. Try again.")

def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            if login(username, password):
                print("Login successful!")
                break  # Exit the loop after successful login
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
