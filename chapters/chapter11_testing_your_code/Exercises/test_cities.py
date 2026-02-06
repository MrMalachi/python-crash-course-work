"""
A file designed to test the 'get_formatted_country' function in city_functions
module.
"""

from city_functions import get_formatted_country

def test_city_country():
    """
    Verify that values such as 'santiago' & 'chile' results in the correct str.
    """
    formatted_country = get_formatted_country("santiago", "chile")
    assert formatted_country == "Santiago, Chile"

def test_city_country_population():
    """Can I include a population argument?"""
    formatted_city_country_population = get_formatted_country(
        "santiago", "chile", 5_000_000
    )
    assert (formatted_city_country_population ==
            "Santiago, Chile - Population 5000000")