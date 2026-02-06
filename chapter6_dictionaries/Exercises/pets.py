# Store these dictionaries in a list called 'pets'
pets = []

# Make several dictionaries, where each dictionary represents a different pet
# In each dictionary, include the kind of animal and the owner's name
dog = {
    "pet name": "rufus", "animal type": "dog", "owner": "nate brown",
    }
pets.append(dog)

cat = {
    "pet name": "ms. whiskers", "animal type": "cat", "owner": "shawna brown",
    }
pets.append(cat)

leopard_gecko = {
    "pet name": "mordecai", "animal type": "leopard gecko", "owner": "malachi brown",
    }
pets.append(leopard_gecko)

gold_fish = {
    "pet name": "guppy", "animal type": "gold fish", "owner": "micah brown",
    }
pets.append(gold_fish)

bird = {
    "pet name": "itachi", "animal type": "bird", "owner": "david simmons",
    }
pets.append(bird)

# Next, loop through your list and as you do, print everything you know about each pet
for animal in pets:
    print(f"\nHere's what I know about {animal["pet name"].title()}:\t")
    for key, value in animal.items():
        print(f"{key}: {value}")