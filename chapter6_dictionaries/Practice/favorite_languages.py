# A Dictionary of Similar Objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

# Creating a new variable 'language' makes for a much cleaner print() call
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

# Utilizing a for loop to iterate through all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

print()

# You can access the value associated with any key you care about inside the loop, by using the current key
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

# Looping Through a Dictionary's Keys in a Particular Order (Alphabetical)
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print()

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
for computer_language in favorite_languages.values():
    print(computer_language.title())

print()

# Make a list of people who should take the favorite languages poll
people = ["malachi", "sarah", "daniel", "phil", "hannah"]

# Loop through the list of people who should take the poll.
# Print a specific message depending on whether a person has/has not taken the poll
for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()} for your response.")
    else:
        print(f"{person.title()}, you are invited to take the poll.")

"""
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
    }
    
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
