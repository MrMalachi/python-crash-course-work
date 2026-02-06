from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text() # # Read the contents of the data file
username = json.loads(contents) # Use json.loads() to assign data to variable.

print(f"Welcome back, {username}!")