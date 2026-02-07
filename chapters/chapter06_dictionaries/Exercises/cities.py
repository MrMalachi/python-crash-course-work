# Make a dictionary called cities & use the names of 3 cities as keys in your dictionary
# Create a dictionary of information about each city AND...
# ...Include:
    # 1. The country that the city is in
    # 2. It's approximate population size
    # 3. One fact about that city
cities = {
    "paris": {
        "country": "france",
        "population": 2000005,
        "fact": "Paris is known to not have any stop signs in the city.",
    },
    "tokyo": {
        "country": "japan",
        "population": 37036000,
        "fact": "Tokyo is home to the world's busiest pedestrian crossing "
                "(Shibuya Crossing).",
    },
    "rome": {
        "country": "italy",
        "population": 4347100,
        "fact": "Modern shopping malls were first invented by the ancient Romans.",
    },
}

# Print the name of each city and all the information you have stored about it
for city, city_info in cities.items():
    print(f"\nCity of {city.title()}:")
    country = city_info["country"].title()
    population = f"{city_info["population"]:,}"
    fact = city_info["fact"]
    print(f"\tCountry - {country} \n\tPopulation Size - {population} \n\tFun Fact - {fact}")




"""
City of Tokyo:
    Country - Japan
    Population Size - 92922929
    Fun Fact - Tokyo is home to....
"""