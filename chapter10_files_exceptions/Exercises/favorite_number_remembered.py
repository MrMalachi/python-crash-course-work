from json import JSONDecodeError
from pathlib import Path
import json

def get_user_info():
    """Prompt user for their info. & return it."""
    while True:
        try:
            phone_number = int(input("Enter your phone number (numbers only): "))
            name = input("Enter your first name: ")
            email = input("Enter your email address: ")
            favorite_tea = input("Enter your favorite type of tea: ")
        except ValueError:
            print("Please enter a valid whole number. Try again...")
        else:
            return name, phone_number, email, favorite_tea

def save_user_info(name, phone_number, email, tea):
    """Save user's info. to JSON file."""
    path = Path("stored_number.json")
    contents = json.dumps([name, phone_number, email, tea])
    path.write_text(contents)

def read_user_info():
    """Orchestrator function."""
    path = Path("stored_number.json")

    try:
        contents = path.read_text()
        name, phone_number, email, tea = (
        json.loads(contents))
        print(
                f"\nName: {name.title()}"
                f"\nPhone Number: {phone_number}"
                f"\nEmail: {email}"
                f"\nFavorite Tea: {tea.title()}"
        )
    except (JSONDecodeError, FileNotFoundError):
        print(f"Your user information hasn't been stored yet.")
        name, phone_number, email, favorite_tea = get_user_info()
        save_user_info(name, phone_number, email, favorite_tea)

read_user_info()
