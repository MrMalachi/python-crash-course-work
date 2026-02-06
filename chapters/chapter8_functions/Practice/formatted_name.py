# The middle_name parameter must be the last argument passed,
# so Python will match up the positional arguments correctly.
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Make sure your positional arguments are in the correct order
musician = get_formatted_name("malachi", "brown", "nathaniel")
print(musician)