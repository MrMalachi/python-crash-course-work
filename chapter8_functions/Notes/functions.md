# CHAPTER 8 | FUNCTIONS

## Defining a Function
* **Function Definition** - tells Python the name of the function and, if applicable, what kind of information
                            the function needs to do its job
  * The parentheses hold this information
* **Body** - the body of the function is any line(s) of code indented after defining the function
* **Docstring** - a comment which describes what the function does
  * When Python generates documentation for the functions in your programs, it looks for a string immediately after the
    function's definition -- usually enclosed in triple quotes for multi-lines
* **Function Call** - when you want to use a function, you must *call* it. This tells Python to execute the code 
                      in the function
```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

### *Passing Information to a Function*
* By modifying the function slightly and including a function definition, you can greet the user by name
```python
# define the function & enter 'username' as the function definition -- this is actually a variable
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# By passing the value 'malachi', it gives the function the information it needs to execute the print() call
greet_user("malachi")
```

### *Arguments and Parameters*
* **Parameter** - a piece of information the function needs to do its job
  * ```python
    # The variable 'username' in the function definition of greet_user() is a parameter
    def greet_user(username):
    ```
* **Argument** - a piece of information that's passed from a function call to a function
  * ```python
    # The value 'malachi' in greet_user("malachi") is an example of an argument 
    greet_user("malachi")
    ```

## Passing Arguments
* **Positional Arguments** - arguments that need to be in the same order the parameters were written 
* **Keyword Arguments** - each argument consists of 1. a variable name 2. a value

### *Positional Arguments*
* When you call a function, Python must match each argument in the function call with a parameter in the function definition
  *  Simplest way to do this -- *positional arguments*
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# When you call 'describe_pet', you need to provide an animal type and a name, in that order
describe_pet("hamster", "harry")
```

#### Multiple Function Calls
* As you can see below, calling a function multiple times is a VERY efficient way to work
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# When you call 'describe_pet', you need to provide an animal type and a name, in that order
describe_pet("hamster", "harry")
describe_pet("dog", "rufus")
```

#### Order Matters in Positional Arguments
* Be sure the order of the arguments in your function call matches the order of the parameters in the function's definition 
  * ```python
    # Example of screwing up the order
    def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

    describe_pet("rufus", "dog")
    ```

### *Keyword Arguments*
* **Keyword Argument** - a name-value pair that you pass to a function... similar to a dictionary
  * *Keyword arguments* help free you from having to worry about correctly ordering your arguments in the function call,
    AND they clarify the role of each value in the function call
* *Keyword arguments* are EXPLICIT, meaning, when you call the function, you explicitly tell Python which parameter
   each argument should be matched with
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# when you call the function, you explicitly tell Python which parameter each argument should be matched with.
describe_pet(animal_type="dog", pet_name="rufus")
describe_pet(pet_name="harry", animal_type="hamster")   # Notice here, the order of keyword arguments DOES NOT matter
```

### *Default Values*
* **Default value** - when defining a default value for each parameter, if an argument for a parameter is provided in 
                      the function call, Python uses the argument value. If not, it uses the parameter's default value, 
                      so when you define a *default value* for a parameter, you can exclude the corresponding argument
                      you'd usually write in the function call
```python
# The definition of 'describe_pet()' includes a default value,
# so now when the function is called with no animal_type specified,
# Python knows to use the value 'dog' for this parameter 
def describe_pet(pet_name, animal_type="dog"):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="rufus")
```
* When you use *default values*, any parameter with a default value needs to be listed after all the parameters that
  DO NOT have *default values*.
  * This allows Python to continue interpreting *positional arguments*

### *Avoiding Argument Errors*
* Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet()  # This produces a TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```

## Return Values
* **Return Value** - the *return* statement takes a value form inside a function and sends it back to the line that 
                     called the function. *Return values* allow you to move much of your program's grunt work into 
                     functions, which can simplify the body of your program

### *Returning a Simple Value*
```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
```
* This might seem like a lot of work to get a neatly formatted name, but when you consider working with larger programs
  that need to store many first and last names separately, functions like 'get_formatted_name()' become very useful

### *Making an Argument Optional*
* Sometimes, it makes sense to make an argument optional, so that people using the function can to choose to provide 
  extra information only if they want to... like a middle name!
```python
# The middle_name parameter must be the last argument passed,
# so Python will match up the positional arguments correctly.
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Make sure your positional arguments are in the correct order
musician = get_formatted_name("malachi", "brown", "nathaniel")
print(musician)
```

### *Returning a Dictionary*
```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
       person["age"] = age
    return person

musician = build_person("jimi", "hendrix", 27)
print(musician)
```

### *Using a Function with a while Loop*
```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your full name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

## Passing a List
```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ["hannah", "tyler", "daniel"]
greet_users(usernames)
```

### *Modifying a List in a Function*
* Every function you create should have one specific job
  * If you're writing a function and notice the function is doing too many different tasks, try to split the code into 
    two different tasks
```python
def print_models(unprinted_designs, completed_models):
    """"
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

```python
# HOW TO MOVE ITEMS FROM A SEPARATE LIST WITHOUT USING FUNCTIONS
# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)
```

### *Preventing a Function from Modifying a List*
* Syntax: *function_name(list_name[:])*
```python
print_models(unprinted_designs[:], completed_models)
```
* The function 'print_models' uses a copy of the original 'unprinted designs' list, not the actual 'unprinted_designs' list
* The list 'completed_models' will fill up with the names of printed models like it did before, but the original list 
  of 'unprinted_designs' will be unaffected by the function.

## Passing an Arbitrary Number of Arguments
* Use an asterisk in the parameter name to pass an arbitrary number of arguments
* **Tuple** - an ordered, immutable collection of items
```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni") # This is a tuple
make_pizza("mushrooms", "green peppers", "extra cheese")    # This is also a tuple
```

### *Mixing Positional and Arbitrary Arguments*
* ***args** - positional arguments are assigned to parameters based on their order in the function call
* If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number
  of arguments must be placed LAST in the function definition
  * Python matches positional & keyword arguments first and then collects any remaining arguments in the final parameter
```python
def make_pizza(size, *toppings):    # The 'size' parameter is first, then follows the arbitrary 'toppings' parameter
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}--inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni") # This is a tuple
make_pizza(12, "mushrooms", "green peppers", "extra cheese")    # This is also a tuple
```

### *Using Arbitrary Keyword Arguments*
* **Key-word Arguments** - a way of passing arguments to a function by explicitly naming the parameter they
                           correspond to within the function call
  * ****kwargs** - used to collect nonspecific keyword arguments
* Double asterisks in the function definition before a parameter are used to tell Python to create a dictionary
  containing all the extra name-value pairs the function receives

```python
def build_profile(first, last, **user_info):    # 'user_info' takes keyword arguments & places them into a dictionary as key-value pairs 
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics")

print(user_profile)
```
#### Important!
* *args VS. **kwargs
  * *args - takes positional arguments & places them into a tuple
  * **kwargs - takes keyword arguments & places them into a dictionary as key-value pairs 

## Storing Your Functions in Modules
* **Module** - a separate file where you store your functions that ends with *.py*
* **Importing** - an *import* statement tells Python to make the code in a module available in the currently running
                  program file
  * Storing your functions in a separate file allows you to hide the details of your program's code and focus on 
    its higher-level logic

### *Importing an Entire Module*
**Syntax**
```python
module_name.function_name()
```
```python
# The import pizza line tells Python to open the file 'pizza.py' and copy 
# all the functions from it into this program
import pizza 

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "ham", "sausage", "extra cheese")
```

### *Importing Specific Functions*
**Syntax**
```python 
from module_name import function_name
```
```python
# Importing more than one specific function
from module_name import function_0, function_1, function_2
```
**making_pizzas.py**
```python
# The import pizza line tells Python to open the file 'pizza.py' and copy
# all the functions from it into this program
from pizza import make_pizza

make_pizza(16, "pepperoni")
make_pizza(12, "ham", "sausage", "extra cheese")
```

### *Using as to Give a Function an Alias*
* **Use-Case**
  * if the function you're importing might conflict with an existing name in your program
  * if the function name is long, you can use a short, unique *alias* - an alternate name similar to a nickname for the function

**Syntax**
```python
from module_name import function_name as fn 
```
**making_pizzas.py**
```python
from pizza import make_pizza as mp  # 'as' keyword allows for aliasing the function

mp(16, "pepperoni")
mp(12, "ham", "sausage", "extra cheese")
```

### *Using as to Give a Module an Alias*
**Syntax**
```python
import module_name as mn
```
**making_pizzas.py**
```python
import pizza as p   # 'as' keyword allows for aliasing the module

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "ham", "sausage", "extra cheese")
```

### *Importing All Functions in a Module*
**Syntax**
```python
from module_name import *
```
**making_pizzas.py**
```python
from pizza import *

make_pizza(16, "pepperoni")
make_pizza(12, "ham", "sausage", "extra cheese")
```

## Styling Functions
**Conventions**
1. Functions should have descriptive names, and these names should use lowercase letters & underscores
   * Module names should use these conventions as well
2. Every function should have a comment that explains concisely what the function does
   * This comment should appear immediately after the function definition & use the docstring format
3. If you specify a default value for a parameter, no spaces should be used on either side of the equals sign

* **Syntax**
    ```
    def function_name(parameter_0, parameter_1="default_value")
    ```
  * The same convention should be used for keyword arguments in the function calls:
  ```python
    function_name(value_0, parameter_1="value")
  ```
4. PEP 8 recommends that you limit lines of code to 79 characters for readability, so if your function's definition is
   lengthy, you can press the ENTER key after opening parenthesis on the definition line
* **Syntax**
    ```python
    def function_name(
            parameter_0, parameter_1, parameter_2,
            parameter_3, parameter_4, parameter_5):
        *function body...*
    ```
5. Separate functions in your program of module IF there is more than one function by using white space
6. All *import* statements dhould be written at the beginning of your file to describe the overall program

