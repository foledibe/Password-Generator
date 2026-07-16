import random
import string
import argparse


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password based on chosen character types."""
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def parse_arguments():
    """Read options the user typed in the terminal."""
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-upper", action="store_false", dest="use_upper", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_false", dest="use_symbols", help="Exclude symbols")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    new_password = generate_password(
        length=args.length,
        use_upper=args.use_upper,
        use_digits=args.use_digits,
        use_symbols=args.use_symbols,
    )
    print("Your generated password is:", new_password)