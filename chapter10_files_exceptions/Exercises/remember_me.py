from json import JSONDecodeError
from pathlib import Path
import json

def get_stored_user_info(path):
    """Get the stored username if available."""
    if path.exists():
        contents = path.read_text()
        username, email, favorite_music = json.loads(contents)
        return username, email, favorite_music
    else:
        return get_new_user_info()

def get_new_user_info(path):
    """Prompt for new user information and return it."""
    user_info = {}
    username = input("What's your name? ")
    email = input("What's your email address? ")
    favorite_music = input("What's your favorite music genre? ")

    contents = json.dumps(user_info)
    path.write_text(contents)
    return username, email, favorite_music


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_user_info(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user_info(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
