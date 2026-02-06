# Import the class 'Path' from the path library.
from pathlib import Path

# Create a Path object that points to the 'learning_python.txt' file.
path = Path("learning_python.txt")
contents = path.read_text() # Read the file into memory and store as one str.

# Convert the single string 'contents' into a list of strings.
# Loop directly over the list, through each string in the list, one at a time.
for line in contents.splitlines():
    line = line.replace("Python", "Java")
    print(line)

"""
.replace() does NOT modify the original string because strings are immutable!
The .replace() method returns a new string and reassigns it back to line.
Only the temporary loop variable 'line' is changed, therefore, this program
only prints the modified version to the screen (console). 
"""



