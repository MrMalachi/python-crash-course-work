major_rivers = {
    "nile": "egypt",
    "amazon": "south america",
    "mississippi": "united states of america",
    }

# Use a loop to print a sentence about each river
for river, region in major_rivers.items():
    print(f"The {river.title()} River runs through {region.title()}.")

print()

# Use a loop to print the name of each river included in the dictionary
for river in major_rivers.keys():
    print(river.title())

print()

# Use a loop to print the name of each country/region included in the dictionary
for region in major_rivers.values():
    print(region.title())


