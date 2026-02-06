pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# while loop removes all instances of the value specified "cat"
while "cat" in pets:
    pets.remove("cat")

print(pets)