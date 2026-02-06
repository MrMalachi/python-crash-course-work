from pathlib import Path

path = Path("session_log.txt")
contents = ""

while True:
    question1 = input("\nWhat did you work on today? ").title()
    question2 = input("How many minutes did you spend on it? ")
    contents += f"Session: {question1} | Time Spent: {question2} minutes\n"

    path.write_text(contents)   # Update the file path with string immediately.

    choice = input("Would you like to add another session? (yes/no): ")
    if choice.lower() == "no":
        break