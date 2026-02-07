def city_country(city, country):
    formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country

print(city_country("santiago", "chile"))
print(city_country("kyoto", "japan"))
print(city_country("rome", "italy"))

