class Restaurant:
    """Simulates a restaurant business."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize instance variables."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 23

    def describe_restaurant(self):
        """Prints the name and type of cuisine of a given restaurant."""
        print(f"\nThis is {self.restaurant_name}."
              f" We serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")

    def set_number_served(self, customers):
        """
        Sets the number of customers that have been served...
        (Modifying an attribute through a method).
        """
        self.number_served = customers

    def increment_number_served(self, additional_customers):
        """
        Increases the number of customers served...
        (Incrementing an attribute's value through a method).
        """
        self.number_served +=  additional_customers

"""
# Make an instance from the Restaurant class
restaurant = Restaurant("Big Kahuna", "Hawaiian")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""