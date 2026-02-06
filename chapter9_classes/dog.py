class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# This creation of an instance is called - 'instantiation'.
my_dog = Dog("Rufus", 14)
your_dog = Dog("Snickers", 12)  # Creation of another instance.

# To access the attributes of an instance, you use dot notation.
print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"{your_dog.name} is {your_dog.age} years old.")
your_dog.sit()
