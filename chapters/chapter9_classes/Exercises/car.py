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

my_used_car = Car("honda", "crv", 2016)
print(my_used_car.get_descriptive_name())

# Modifying the value of an attribute (self.odometer_reading) through a method
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# Incrementing the value of an attribute through a method
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
