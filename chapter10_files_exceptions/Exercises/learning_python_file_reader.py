# From the path library (module), import the Path class.
# Remember, a library is a module, but with a very specific use-case.
from dataclasses import replace
from pathlib import Path

# Write a program that prints the contents once by reading in the entire file.
path = Path("learning_python.txt")  # Create an instance to do a system call.
# Use the method 'read_text()' on the object to read the file.
contents = path.read_text()

print(contents) # Display the entire contents of the .txt file.

# Create an empty str to build a new str piece-by-piece.
learning_python_string = ""
# For each str inside the list 'lines', do the following...
for line in contents.splitlines():  # Loop directly over the returned list.
    learning_python_string += line  # String concatenation.

print(learning_python_string)

