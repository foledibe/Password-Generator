import random
import string


def generate_password(length=12):
    """Generate a random password of the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    new_password = generate_password()
    print("Your generated password is:", new_password)