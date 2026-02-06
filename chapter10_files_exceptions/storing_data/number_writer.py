from pathlib import Path
import json # Import the json module that allows us to convert.

numbers = [2, 3, 5, 7, 11, 13]  # The list we want to convert.

path = Path("numbers.json") # Choose a filename in which to store the list.
contents = json.dumps(numbers)  # Generate a string that is the JSON equivalent
path.write_text(contents)   # Use the method to write to the file.