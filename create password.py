import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (default is 12): "))
    except ValueError:
        length = 12  # Default length if input is invalid
    print(f"Generated Password: {generate_password(length)}")