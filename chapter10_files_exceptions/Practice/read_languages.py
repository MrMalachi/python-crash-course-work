from pathlib import Path

path = Path("languages.txt")

# Read the entire .txt file at once.
contents = path.read_text()

# Print each language with the first letter capitalized.
print(contents.title() + "\n")

# Store the lines in a list (store each line of text in a list).
lines = contents.splitlines()

# Loop through the list and print each language in uppercase.
for line in lines:
    print(line.upper())



