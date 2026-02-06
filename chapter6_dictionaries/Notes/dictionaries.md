# CHAPTER 6 | DICTIONARIES

## A Simple Dictionary
```python
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])
```

## Working with Dictionaries
* **Dictionary** - a collection of *key-value pairs*, where each key is connected to a value
* **Key-value pair** - a set of values associated with each other 
  * ```python
    alien_0 = {"color": "green"}
    ```

### *Accessing Values in a Dictionary*
* Give the name of the dictionary & then place the key inside a set of square brackets
```python
# Accessing the value 'color' of the alien
alien_0 = {"color": "green"}
print(alien_0["color"])

# Accessing the value 'points' of the alien
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
```

### *Adding New Key-Value Pairs*
```python
alien_0 = {"color": "green", "points": "5"}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
```

### *Starting with an Empty Dictionary*
```python
# This method is used when writing code that generates a large number of keys or when storing user-supplied data
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)
```

### *Modifying Values in a Dictionary*
```python
alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}.")
```
#### Tracking the Position of an Alien Moving at Different Speeds
```python
# Tracking the position of an alien that can move at different speeds
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0["x_position"]}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position + the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0["x_position"]}")
```
### *Removing Key-Value Pairs*
```python
alien_0 = {"color": "green", "points": "5"}
print(alien_0)

del alien_0["points"]
print(alien_0)
```

### *A Dictionary of Similar Objects*
```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

# Creating a new variable 'language' makes for a much cleaner print() call
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")
```

### *Using get() Method to Access Values*
```python
alien_0 = {"color": "green", "speed": "slow"}
print(alien_0["points"])    # intentional KeyError

# get() method
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)
```

## Looping Through a Dictionary
* **.items()** method - returns a sequence of key-value pairs

### *Looping Through All Key-Value Pairs*
```python
user_0 = {
    "username": "BrownBEAST4",
    "first": "malachi",
    "last": "brown",
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

### *Looping Through All the Keys in a Dictionary*
* **.keys()**  method - explicitly returns a sequence of keys without any values 

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

for name in favorite_languages.keys():
    print(name.title())
```

### *Looping Through a Dictionary's Keys in a Particular Order (Alphabetical)*
```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

### *Looping Through All Values in a Dictionary*
* **.values()** method - returns a sequence of values without any keys
```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

print("The following languages have been mentioned:")
for computer_language in favorite_languages.values():
    print(computer_language.title())
```
* **.set()** function - a collection in which each item must be unique (does not show duplicate values)
```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

for language in set(favorite_languages.values()):
    print(language.title())
```

## Nesting 
### *A List of Dictionaries*
```python
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```
#### More Realistic Approach
```python
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Make the first 3 green aliens to yellow
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    # Turn yellow aliens into red, fast-moving ones worth 15 points using an elif block
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
```

### *A List in a Dictionary*
* **Nesting** - placing one programming construct inside another
  * You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key in a dictionary
* You should **NOT** nest lists & dictionaries too deeply... there's most likely a simpler way to solve the problem
```python
# Store information about a pizza being ordered: Nested list within a dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
    }

# Summarize the order
print(f"You ordered a {pizza["crust"]}-crust pizza "
        "with the following toppings: ")

for topping in pizza["toppings"]:
    print(f"\t{topping}")
```

#### Nested 'for' Loop
```python
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
    }
    
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
```

### *A Dictionary in a Dictionary*
```python
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
        },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
        },
}

for username, user_info in users.items():
    print(f"\nUsrname: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```
