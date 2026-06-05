import random
import string

def generate_password():
    try:    # Handle invalid inputs (non-integer values)
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.\n")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)

    except ValueError:    # Handle non-integer inputs
        print("Please enter a valid number.")

generate_password()
