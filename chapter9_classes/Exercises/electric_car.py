class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # assigning a default value to instance attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        # print vs return:
        # could this value ever be used for anything other than immediate display?
        # If yes? return it. If no? print() is fine.
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount (eventually the argument) to the odometer reading."""
        # self.odometer_reading = self.odometer_reading + miles
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    # Optional parameter 'battery_size' set IF no value is provided
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # Attributes of the parent class.
        # Assign the instance 'Battery()' to the attribute self.battery.
        # This allows you to work through the car's battery attribute,
        # when you create an electric car and want to describe the battery.
        self.battery = Battery()

# Make an instance of the ElectriCar class and assign it to 'my_leaf'.
my_leaf = ElectricCar("nissan", "leaf", 2025)
print(my_leaf.get_descriptive_name())

# Call the method that's associated with the Battery() instance assigned to
# the attribute to display the vehicles battery size & battery range.
my_leaf.battery.describe_battery()
my_leaf.battery.get_range() # Must be called THROUGH the car's battery attribute.


