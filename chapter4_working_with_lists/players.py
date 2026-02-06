# Slicing - Python automatically starts the slice at the beginning of the list since the first index is omitted

players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[:4])

# Looping through a slice
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())