# Import the Path class from the pathlib library (module).
from pathlib import Path

# Adds the value of the right-hand operand to the left-hand operand and then
# assigns the new result back to the left-hand operand.
# contents = contents + "string"
contents = "I love programming!\n"  # Define variable to hold contents of file.
contents += "I love creating new software programs.\n"
contents += "I also love working with data.\n"

# Create an instance of 'Path'
path = Path("programming.txt")
# Use the write_text() method to write the value of contents to the file.
path.write_text(contents)
