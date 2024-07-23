#!/usr/bin/python3

"""" generating random pasword for a given lenght.
Using the inbuilt "Random" and "String" functions and
My own function password_generator.py"""


import password_generator

length = int(input("Enter desired password length: "))
password = password_generator.generate_complex_password(length)
print(f"Generated Password: {password}")
