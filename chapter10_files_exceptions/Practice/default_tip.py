from json import JSONDecodeError
from pathlib import Path
import json

path = Path("tip_pref.json")    # Create an instance (a path).

def save_tip_preference(tip_percent):
    """Write tip percentage to JSON file."""
    # Write what the user passes as an argument in to the file.
    contents = json.dumps(tip_percent)
    path.write_text(contents)

def load_tip_preference():
    """Load the user's tip preference if it exists and is valid."""
    if not path.exists():
        return None  # Explicitly return nothing if file exists.

    try:
        contents = path.read_text()
        return json.loads(contents)
    except JSONDecodeError:
        return None

tip = load_tip_preference()

if tip is not None:
    print(f"Your saved tip preference is {tip}%")

else:
    print(f"You do not have a saved tip preference.")
    tip = int(input("Enter your default tip percent: "))

    save_tip_preference(tip)
    print(f"{tip}% has been saved!")

