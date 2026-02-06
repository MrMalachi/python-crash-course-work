from json import JSONDecodeError
from pathlib import Path
import json

def get_username():
    """Prompt user for a username & return a string."""
    username = input("Enter your username: ")

    return username

def save_username(username):
    """Save the username to JSON file."""
    path = Path("username.json")
    contents = json.dumps(username)
    path.write_text(contents)

def load_username():
    """Read JSON file and return username. Raise or handle errors."""
    path = Path("username.json")

    try:
        contents = path.read_text()
        username = json.loads(contents)
    except (FileNotFoundError, JSONDecodeError):
        print(f"{path} does not exist. Creating it now...")
        path.write_text("")
    else:
        print(f"Welcome {username}!")
        return username

def login_user():
    """
    Orchestrator Function tries to load username:
    if it exists, print a message.
    if not, ask user, save it, and welcome them.
    """
    username = load_username()

    if username:
        print(f"Welcome {username}!")
        return
    else:
        print("Your username has not been saved yet.")
        username = get_username()
        save_username(username)

login_user()