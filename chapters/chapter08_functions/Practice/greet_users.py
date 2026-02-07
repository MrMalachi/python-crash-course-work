def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ["malachi", "hannah", "tyler"]

greet_user(usernames)