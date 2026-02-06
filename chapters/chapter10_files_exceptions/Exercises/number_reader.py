from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)  # Pass the contents of the file to json.loads()
                                # Take a formatted str & return a Python object

print(numbers)  # Display the data shared between two programs