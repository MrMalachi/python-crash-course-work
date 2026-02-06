# Keys: Name, Age, Location, Favorite Video-Game Console
responses = {}

print("\n--- VIDEO-GAME CONSOLE POLL ---")

while True:
    name = input("What is your first and last name? ").title()
    age = int(input("How old are you? "))
    location = input("What country do you reside in? ").title()
    favorite_console = input("What is your favorite video-game console? ").title()
    repeat = input("Would you like to let another person respond? (yes / no) ")

    # Store ALL user input (data) inside a nested dictionary.
    # The key 'name' is the unique identifier & nested within this key/value,
    # are other keys and values: age, location, favorite console.
    user_profile = {
        "age": age,
        "location": location,
        "favorite console": favorite_console,
    }

    # Store the nested dictionary 'user_profile' in the outer dictionary 'responses'
    responses[name] = user_profile

    if repeat == "no":
        break

print("\n--- POLL RESULTS ---")

for name, personal_info in responses.items():
    print(f"\n{name}:")
    for key, value in personal_info.items():
        print(f"\t{key.title()} - {value}")










