# Sample user data (hashed passwords for demonstration only, never store plain text!)
users = {
    "user1": "$2b$12$0wlzOPWNzZI5Kbu.s9Qvwu..es.T/zHTK....x..s.../K..y.....",  # Hashed password for "password1"
    "user2": "$2b$12$y82hONaCzJbMYx..AL..OePhV.Ck....v..x..s.../K..y....."   # Hashed password for "password2"
}

# Failed login attempt limit and lockout duration (minutes)
max_attempts = 3
lockout_duration = 15

def login():
  username = input("Username: ")
  password = input("Password: ")

  # Validation for empty fields
  if not username or not password:
    raise ValueError("Username and password cannot be empty")

  # Check if username exists
  if username not in users:
    raise ValueError("Invalid username")

  # Access user data
  user_data = users[username]

  # Login attempt counter (stored outside the function for persistence)
  failed_attempts = get_failed_attempts(username)

  # Check for locked account
  if failed_attempts >= max_attempts:
    lockout_time = get_lockout_time(username)
    if is_locked_out(lockout_time):
      raise PermissionError(f"Account locked for {lockout_duration} minutes due to failed attempts. Try again later.")

  # Verify password (assuming a secure hashing function is used for storage)
  # Replace with your password verification logic using the actual hashing function
  if not verify_password(password, user_data):
    # Increment failed attempts and update lockout time
    update_failed_attempts(username)
    raise PermissionError("Invalid password")

  # Login successful
  print("Login successful!")

  # Reset failed attempts for future logins
  reset_failed_attempts(username)

# Simulate storing and retrieving failed attempts (replace with actual storage mechanism)
def get_failed_attempts(username):
  # Example: retrieve data from a database or session variable
  return 0  # Replace with actual retrieval logic

def update_failed_attempts(username):
  # Example: update data in a database or session variable
  pass  # Replace with actual update logic

def reset_failed_attempts(username):
  # Example: reset data in a database or session variable
  pass  # Replace with actual reset logic

# Simulate storing and retrieving lockout time (replace with actual storage mechanism)
def get_lockout_time(username):
  # Example: retrieve data from a database or session variable
  return None  # Replace with actual retrieval logic

def is_locked_out(lockout_time):
  # Check if lockout time is within the lockout duration
  if lockout_time is None:
    return False
  # Replace with logic to compare lockout_time with current time and lockout_duration
  return False  # Replace with actual lockout check

# Replace this with your actual password verification logic using a secure hashing function
def verify_password(password, user_data):
  # This is just a placeholder for demonstration, never compare plain text passwords!
  return password == user_data.split("$")[2]  # Assuming password is stored in a specific format

# Main program flow
while True:
  try:
    login()
    break
  except (ValueError, PermissionError) as e:
    print(f"Error: {e}")
    print("Please try again.")

