# Practice storing & retrieving data with JSON using functions by:
    # Building a simple app that remembers a user's preferred display mode

from pathlib import Path
import json

def get_displayed_preference():
    """Prompts user to choose a light or dark display."""
    display_preference = input("Do you prefer a light or dark display mode? ").strip().lower()
    return display_preference

def save_preference(preference):
    """Serialize (convert to string) the preference and save it to a file."""
    path = Path("display_pref.json")
    contents = json.dumps(preference)
    path.write_text(contents)

def load_preference():
    """Reads the json file and returns the user's stored preference."""
    path = Path("display_pref.json")
    contents = path.read_text()
    return json.loads(contents)

preference = load_preference()

if preference:
    print(f"Loaded preference: {preference}")
else:
    preference = get_displayed_preference()
    save_preference()

