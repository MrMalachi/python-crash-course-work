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

class IceCreamStand(Restaurant):
    """
    A child class inheriting the original 'Restaurant' class because
    an ice cream stand is a specific kind of restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """
        Initialize parent class attributes.
        Initialize child class attribute that stores ice cream flavors in a list.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Displays ice cream flavors."""
        print(f"Ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Create an instance of IceCreamStand.
brain_freeze = IceCreamStand("brain freeze")

# Replace the 'flavors' attribute on the brain_freeze object with a new list.
brain_freeze.flavors = ["vanilla", "chocolate", "strawberry"]

brain_freeze.describe_restaurant()
brain_freeze.show_flavors()



