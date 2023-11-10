#RandomPasswordGenerator

import random
import string

def generate_password(length, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    try:
        length = int(input("Enter the password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, uppercase, digits, special_chars)
        print("\nGenerated Password: {}".format(password))
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()