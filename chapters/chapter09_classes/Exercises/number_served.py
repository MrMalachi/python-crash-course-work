class Restaurant:
    """Simulates a restaurant business."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize instance variables."""
        self.restaurant_name = restaurant_name
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

# Create an instance called 'restaurant' from the Restaurant class.
restaurant = Restaurant("Soul Sucker", "Soul Food")

# Print the number of customers the restaurant has served (default attribute value=23).
print(restaurant.number_served)

# Call the set_number_served() method on the instance with a new number (argument).
restaurant.set_number_served(46)

# Print the value of the attribute 'number_served' again.
print(restaurant.number_served)

# Call the increment_number_served() method on the instance with any number
# to increase the number_served attribute. This will combine the set_number_served
# value (argument) '46' and the value you, the caller provide (100) when making
# the argument for the increment_number_served.
restaurant.increment_number_served(100)

# Display the total number of customers served in a business day.
print(restaurant.number_served)


