print("Hello Welcome to the Password Generator")

# Create a input for user_name
username = input("What is your name?")

# Create a input for password
password = input("What is your password?")

# Create a password length for learn password length
password_length = len(password)

# Create a hidden password and use password length for hide password
hidden_password = "*" * password_length

print(f"{username} your password, {hidden_password}, is {password_length} letters long")