"""A program utilizing the restaurant module."""

from restaurant import Restaurant

# Create three different instances from the Restaurant class
mexican_restaurant = Restaurant("Loco Moco", "Mexican")
japanese_restaurant = Restaurant("Lucky Danger", "Japanese")
american_restaurant = Restaurant("1950", "American")

# Call describe_restaurant() method for each instance
mexican_restaurant.describe_restaurant()
japanese_restaurant.describe_restaurant()
american_restaurant.describe_restaurant()
