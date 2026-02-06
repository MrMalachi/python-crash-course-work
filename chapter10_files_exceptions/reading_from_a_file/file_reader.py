# import the Path class from the module (library) 'pathlib'.
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

# Loop directly over the list that is created when using 'splitlines()' method.
for line in contents.splitlines():  # For every string in the list, print(line)
    print(line)

