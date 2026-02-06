# Make a dictionary called 'favorite_places'
# Think of 3 names to use as keys in the dictionary...
# ...And store 1 - 3 favorite places for each person
# Ask some friends to name a few of their favorite places
favorite_places = {
    "jairus": ["boxing gym"],
    "malachi": ["movie theater", "boba tea shop", "gym"],
    "kristan": ["movie theater", "hair salon"],
    "elisha": ["gun range", "gym"],
    }

# Loop through the dictionary and print each person's name & their favorite place(s)
for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{person.title()}'s favorite place is: ")
        print(f"\t{places[0]}")
    else:
        print(f"\n{person.title()}'s favorite places are: ")
        for place in places:
            print(f"\t{place}")

