# CHAPTER 9 | CLASSES

## Glossary
* **Class** - a set of instructions (blueprint) that tells Python how to make an instance
  * Ex). The `Dog` class is a set of instructions that tells Python how to make individual instances 
         representing specific dogs
* **Instance** - a specific, individual *object* created from a class (specific)
  * Emphasizes where it came from
* **Initialize** - set to th value or put in the condition appropriate to the start of an operation
* **Object** - a thing that exists in memory with data & behavior (broader)
  * Emphasizes what it is
* **Instantiation** - making an object (instance) from a class
* **Method** - a function that's part of a class
* `__init__()` - a special method that Python runs automatically whenever we create
  a new instance based on the `Dog` class
* `self` - a required parameter in the method definition because when Python calls
  this method later (to create an instance), the method call will automatically
  pass the `self` argument.
  * It gives the individual instance access to the attributes and methods in the class
* **Attributes** - variables that are accessible through instances 
  * The value associated with the parameter is assigned to the variable, which is then attached to the instance
    being created
  * **Instance Attributes** - when an instance is created, attributes can be defined without being passed in as 
    parameters
* **Increment** - the action of changing the value of a variable so that it increases
* **Inheritance** - a *child* class, taking on the attributes and methods of the *parent* class
  * A child class can also define new attributes and methods of its own
* **super()** - a special function that allows you to call a method from the parent class
  * **superclass** - an older convention name for the parent class
  * **subclass** - an older convention name for the child class
* **Composition** - breaking your large class into smaller classes that work together when your large (main) class
                    becomes lengthy
* **Software of Concerns (SoC)** - a fundamental software design principle for breaking complex systems into
                             distinct, independent modules, each handling a single "concern" (like UI, data storage,
                             or business logic) to improve maintainability, scalability, and focus.     
* **Python standard library** - a set of modules included with every Python installation that you can utilize

## Creating and Using a Class

### *Creating the Dog Class*
* Each instance created from the `Dog` class will store a `name` and an `age`, and
  we'll give each dog the ability to `sit()` and `roll_over()`

**dog.py**
```python
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
```

### *Making an Instance from a Class*
```python
class Dog:
    --snip--
    
my_dog = Dog("Rufus", 14)   # This creation of an instance is called - 'instantiation'
```

#### Accessing Attributes
* To access the attributes of an instance, you use dot notation
* Python looks at the instance `my_dog` and then finds the attribute `name` asscociated with `my_dog`
```python
class Dog:
    --snip--

my_dog = Dog("Rufus", 14)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

#### Calling Methods
* When Python reads a method call, it looks for the method in the class and runs that code
```python
class Dog:
    --snip--
    
my_dog = Dog("Rufus", 14)

# Using dot notation to call any method defined in the class 'Dog'
my_dog.sit()
my_dog.roll_over()
```

#### Creating Multiple Instances
* You can create as many instances from a class as you need that are capable of the same set of actions
```python
class Dog:
    --snip--

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
```

## Working with Classes and Instances
* Modifying the attributes of an instance directly **VS**. Writing methods that update attributes in specific ways
  * Directly - if it's just data, direct access is fine
  * Methods - if changing a value has rules (like a car odometer that can't be rolled back) use a method

### *The Car Class*

**car.py**
```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        # print vs return:
        # could this value ever be used for anything other than immediate display?
        # If yes? return it. If no? print() is fine.
        return long_name.title()

my_new_car = Car("audi", "q5", 2025)

print(my_new_car.get_descriptive_name())
```

### *Setting a Default Value for an Attribute*

* When an instance is created, attributes can be defined without being passed in as parameters

**car.py**
```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # assigning a default value to instance attribute

    def get_descriptive_name(self):
        --snip--

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car("audi", "q5", 2025)

print(my_new_car.get_descriptive_name())

# Call the newly created method that reads the default value of the instance attribute on my_new_car 
my_new_car.read_odometer()  
```

### *Modifying Attribute Values*

* Three ways to change an attribute's value:
  1. Modify the value directly through an instance
  2. Modify the value through a method
  3. Modify the value by incrementing a method

#### 1. Modifying an Attribute's Value Directly

**car.py**
```python
class Car:
    --snip--

my_new_car = Car("audi", "q5", 2025)
print(my_new_car.get_descriptive_name())

# Modifying the value of an attribute directly through the instance itself
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### 2. Modifying an Attribute's Value Through a Method

**car.py**
```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        # This method takes in a mileage value & assigns it to self.odometer_reading.
        # So, now the new value of self.odometer_reading is whatever
        # the caller enters as an argument for this new method.
        self.odometer_reading = mileage

my_new_car = Car("audi", "q5", 2025)
print(my_new_car.get_descriptive_name())

# Modifying the value of an attribute through a method
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

##### *Adding More Logic*

* Make sure no one tries to roll back the odometer reading by adding a conditional if-else statement

**car.py**
```python
class Car:
    --snip--

        def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car("audi", "q5", 2025)
print(my_new_car.get_descriptive_name())

# Modifying the value of an attribute through a method
my_new_car.update_odometer(22_999)
my_new_car.read_odometer()
```

#### 3. Incrementing an Attribute's Value Through a Method

**car.py**
```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        --snip--

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
```

## Inheritance

### *The init() Method for a Child Class*
* An electric car is just a specific kind of car, so we only have to write code for the attributes and behaviors
  specific to electric cars by using a child class
* The parent class must either be part of the current file and appear before the child class OR
  the parent class must be imported from a module

**electric_car.py**
```python
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

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) # Attributes of the parent class.

# Make an instance of the ElectriCar class and assign it to 'my_leaf'.
my_leaf = ElectricCar("nissan", "leaf", 2025)   
print(my_leaf.get_descriptive_name())
```

### *Defining Attributes and Methods for the Child Class*
* Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary
  to differentiate the child class from the parent class

**electric_car.py**
```python
class Car:
    --snip--

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # Attributes of the parent class.
        self.battery_size = 40  # Default attribute for the ElectricCar class

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Make an instance of the ElectriCar class and assign it to 'my_leaf'.
my_leaf = ElectricCar("nissan", "leaf", 2025)
print(my_leaf.get_descriptive_name())

# Call the method 'describe_battery' on the object.
my_leaf.describe_battery()
```

### *Overriding Methods from the Parent Class*
* To override any method from the parent class that doesn't fit what you're trying to model with the child class,
  you define a method in the child class with the same name as the method you want to override in the parent class
  * Python will disregard the parent class method and only pay attention to the method you define in the child class
  * When you use inheritance, you can make your child classes retain what you need and override anything you don't need
    from the parent class

**electric_car.py**
* Pretend the `Car` class had a method called `fill_gas_tank()`. This method is meaningless for an all-electric vehicle,
  so you might want to override this method... here's one way to do that:
```python
class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't have a gas tank!")
```

### Hard-Coded Attributes vs. Default Parameters

**hard_coded_attribute**
```python
 class Battery:
    
    def __init__(self):
        self.battery_size = 40
```
* **Hard-Coded Attributes** - hard-coding inside the body is only good when the value should *never* change by the
                              caller and is purely internal
  * Every `Battery` object is **forced** to be 40 kWh
  * You **cannot** change it at creation time
  * You'd have to modify it *after* the object exists
```python
battery = Battery()
battery.battery_size = 75   # manual override (not ideal, rigid design)
```

**default_parameter**
```python
class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size
```
* **Default (Optional) Parameter** - if an attribute might reasonably change per object, it belongs in init() as a 
                                     parameter - possibly with a default value
  * Gives you a **default value** (40)
  * You have the **option** to override it when creating the object
```python
battery1 = Battery()    # defaults to 40
battery2 = Battery(75)  # explicitly set to 75 (flexible design)
```

### *Instances as Attributes*

* An instance can be stored as an attribute, and you can call its methods through that attribute:
  * `self.battery = Battery()`
  * `my_leaf.battery.describe_battery()`
* This may look like a lot of extra work, but now we can describe the battery in as much detail as we want
  without cluttering the `ElectricCar` class
* Implementing **Separation of Concerns**, so each class has one clear responsibility

**electric_car.py**
```python
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    # Optional parameter 'battery_size' set IF no value is provided
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

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

# Call the method that's associated with the Battery() instance assigned to the attribute.
my_leaf.battery.describe_battery()
```

#### Add Another Method to Battery

* This method reports the range of the car based on the battery size

**electric_car.py**
```python
class Car:
    --snip--

class Battery:
    --snip--
    
    def get_range(self):
    """Print a statement about the range this battery provides."""
    if self.battery_size == 40:
        range = 150
    elif self.battery_size == 65:
        range = 225

    print(f"This car can go about {range} miles on a full charge.")

class Electric(Car):
    --snip--

# Make an instance of the ElectriCar class and assign it to 'my_leaf'.
my_leaf = ElectricCar("nissan", "leaf", 2025)
print(my_leaf.get_descriptive_name())

# Call the method that's associated with the Battery() instance assigned to
# the attribute to display the vehicles battery size & battery range.
my_leaf.battery.describe_battery()
my_leaf.battery.get_range() # Must be called THROUGH the car's battery attribute.
```

### The Python Standard Library

* Included with every Python installation
* Module `random`


How to generate a random number between 1 & 6:

**randint() function**
```commandline
>>> from random import randint
>>> randint(1, 6)
```

How to take a list or tuple and return a randomly chosen element: 

**choice() function**
```commandline
>>> from random import choice
>>> players = ["charles", "shaq", "michael", "kobe", "kyrie"]
>>> first_up = choice(players)
>>> first_up
OR 
>>> print(choice(players))
```