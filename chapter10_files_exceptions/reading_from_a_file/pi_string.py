from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""  # Create a variable to hold the digits of 'pi'.
for line in lines:  # A loop that adds each line of digits to 'pi_string'.
    pi_string += line.strip()   # Use '.lstrip()' the whitespace that was on
                                # the left side of the digits in each line.

# Print by slicing from index 0, up to but not including index 52.
print(f"{pi_string[:52]}...")
print(len(pi_string))   # Print how long the string is (36 characters).

