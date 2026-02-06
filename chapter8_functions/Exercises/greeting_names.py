names_list = ["malachi", "elisha", "hezekiah", "micah", "jason"]

def greet_user(names):
    """Print a greeting for each name in the provided list."""
    for name in names: # Loop through the list and display a greeting
        print(f"What's up {name.title()}!")

greet_user(names_list)