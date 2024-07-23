import Random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def is_password_complex(password):
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    symbols = any(char in string.punctuation for char in password)
    return all([uppercase, lowercase, digits, symbols])

def generate_complex_password(length):
    password = generate_password(length)
    while not is_password_complex(password):
        password = generate_password(length)
    return password
