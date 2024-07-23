#!usr/bin/python3/

""" This program  repeatedly asks the user for input values until a valid data is entered. It also handles exceptions for invalid types, out-of-range values, and incorrect formats."""

def get_valid_input(prompt, data_type, min_val=None, max_val=None, valid_format=None):
    while True:
        try:
            # Get user input
            value = input(prompt)

      # Convert to the specified data type
            if data_type == int:
                value = int(value)
            elif data_type == float:
                value = float(value)
      # Check for valid format
            if valid_format is not None and value not in valid_format:
                raise ValueError(f"Error: Value must be one of {valid_format}")
            # Check for range
            if min_val is not None and value < min_val:
                raise ValueError(f"Error: Value is too low, try again")
            if max_val is not None and value > max_val:
                raise ValueError(f"Error: Value is too high, try again")
            return value
        except ValueError as e:
            print(e)

# validating the user input and  range
age = get_valid_input("Enter your age: ", int, min_val=18, max_val=100)
print(f"You are the right age for this program")

"""
# Example usage (string with valid values)
color = get_valid_input("Enter your favorite color (red, green, blue): ", str, valid_format=["red", "green", "blue"])
print(f"Your favorite color is: {color}")"""
