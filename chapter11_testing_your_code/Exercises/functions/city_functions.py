# A module designed to be used by a test.

def get_formatted_country(city, country, population=0):
    """Generate a neatly formatted country/city name."""
    city_country = f"{city}, {country}"

    if population:
        city_country += f" - population {population}"

    return city_country.title()
