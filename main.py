import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def generatePassword(length: int, characters: str) -> str:
    return "".join([secrets.choice(characters) for _ in range(length)])

def main():
    count = int(input("Password count: "))
    length = int(input("Password length: "))
    characters = ""
    if input("Use uppercase? [y/n] ").lower() == "y":
        characters += ascii_uppercase
    if input("Use lowercase? [y/n] ").lower() == "y":
        characters += ascii_lowercase
    if input("Use digits? [y/n] ").lower() == "y":
        characters += digits
    if input("Use punctuation? [y/n] ").lower() == "y":
        characters += punctuation
    for index in range(count):
        print(f"[{index + 1}] {generatePassword(length, characters)}")

if __name__ == "__main__":
    main()