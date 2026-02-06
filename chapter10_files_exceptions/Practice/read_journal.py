from pathlib import Path

path = Path("journal.txt")
contents = ""   # Create an empty string to hold all the data (accumulator str)

while True:
    journal_entry = input("Please type your journal entry below:\n")
    # Add received input to the string 'contents' in a formatted way.
    contents += f"Entry: {journal_entry}\n\n"
    path.write_text(contents)   # Update the file by writing text immediately.

    choice = input("Would you like to add another entry? (yes/no): ")
    if choice.lower() == "no":
        break