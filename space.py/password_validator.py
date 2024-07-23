def password_length(password, min_length=6):
    return len(password) >= min_length

def password_complexity(password):
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digits = any(char.isdigit() for char in password)
    special_chars = any(not char.isalnum() for char in password)
    return all([uppercase, lowercase, digits, special_chars])

def validate_password(password):
    return all([password_length(password), password_complexity(password)])
