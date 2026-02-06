from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""  # Create a variable to hold the digits of 'pi'.
for line in lines:  # A loop that adds each line of digits to 'pi_string'.
    pi_string += line.strip()

# Prompt for the user's birthday, and then check if that str is in 'pi_string'.
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
