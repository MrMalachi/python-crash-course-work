from pathlib import Path

# Prompt user for their name.
contents = input("Enter your name: ").title()

# Instantiate so you can create a file-path.
path = Path("guest.txt")

# Write the content string to the file (object).
path.write_text(contents)