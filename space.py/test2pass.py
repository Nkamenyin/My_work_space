user_data = {
            "user1": {
                        "password": "password1",
                                "attempts": 0,
                                        "locked": False
                                            },
                "user2": {
                            "password": "password2",
                                    "attempts": 0,
                                            "unlock_time": None  # Optional: unlock time for locked accounts
                                                }
                }
def login(username, password):
      if not username or not password:
              raise ValueError("Username and password cannot be empty")

            if username not in user_data:
                    raise Exception("Invalid Username")

                  user = user_data[username]

                    if user["locked"]:
                            # Check if unlock time has passed (optional)
                                if user.get("unlock_time") and time.time() > user["unlock_time"]:
                                          user["locked"] = False
                                                user["attempts"] = 0  # Reset attempts on unlock
                                                    else:
                                                              raise Exception("Account Locked. Try Again Later")

                                                            if user["password"] != password:
                                                                    user["attempts"] += 1
                                                                        if user["attempts"] >= 3:
                                                                                  user["locked"] = True
                                                                                        raise Exception("Account Locked. Too many failed attempts")
                                                                                        else:
                                                                                                  raise Exception("Invalid Password")

                                                                                                # Login successful (logic omitted for security reasons)
                                                                                                  print(f"Welcome, {username}!")

try:
      login("user1", "correct_password")  # Successful login
except (ValueError, Exception) as e:
      print(f"Login Error: {e}")
