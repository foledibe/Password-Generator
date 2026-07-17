# Password Generator

A command-line tool built in Python that generates secure, customizable random passwords and rates their strength.

## Features

- Adjustable password length
- Toggle uppercase letters, digits, and symbols on/off
- Option to avoid visually ambiguous characters (l, I, 1, O, 0)
- Built-in password strength checker

## How to Run

Basic usage (generates a 12-character password with all character types):

```bash
python password_generator.py
```

Custom length:

```bash
python password_generator.py --length 20
```

Avoid confusing characters like l, I, 1, O, 0:

```bash
python password_generator.py --avoid-ambiguous
```

Exclude symbols or digits:

```bash
python password_generator.py --no-symbols --no-digits
```

Combine options:

```bash
python password_generator.py --length 16 --avoid-ambiguous --no-symbols
```

## All Options

| Flag                | Description                                         |
| ------------------- | --------------------------------------------------- |
| `-l`, `--length`    | Set password length (default: 12)                   |
| `--no-upper`        | Exclude uppercase letters                           |
| `--no-digits`       | Exclude digits                                      |
| `--no-symbols`      | Exclude symbols                                     |
| `--avoid-ambiguous` | Avoid visually confusing characters (l, I, 1, O, 0) |

## Example Output

```
Your generated password is: xK9#mPq2$vNz
Strength rating: Very Strong
```

## What I Learned

This project helped me practice working with Python's `random`, `string`, and `argparse` libraries, along with using Git and GitHub for version control. I also learned how to design a command-line interface with multiple configurable options and how to build simple scoring logic for the strength checker.

## Author

Fiorella Oledibe
