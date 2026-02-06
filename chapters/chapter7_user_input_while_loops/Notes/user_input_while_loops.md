# CHAPTER 7 | USER INPUT & WHILE LOOPS

## How the input() Function Works
* **Prompt** - instructions for a user to follow
```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

### *Writing Clear Prompts*
```python
# Pythonic Way
# Writing a prompt longer than one line
prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

```python
# Remedial Way
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

### *Using int() to Accept Numerical Input*
* **int()** - built-in function allowing you to convert a *string* to and *integer*
```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

### *The Modulo Operator*
* **modulo(%)** - a useful tool which divides one number by another number and returns the remainder

## Introducing while Loops
* **while loop** - contrary to a **for loop** that takes a collection of items & executes a block of code once for each
                    item in the collection 
  * A **while loop** runs as long as, or *while*, a certain condition is true
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # current_number = current_number + 1
```

### *Letting the User Choose When to Quit*
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":   # the message only prints if it DOES NOT match the quit value
        print(message)
```

### *Using a Flag*
* **flag** - acts as a signal to the program when it has many different events that could cause the program to stop running
  * For a program that should run only as long as many conditions are true, you can define one variable that determines
    whether or not the entire program is active
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True   # as long as the active variable remains True, the loop will continue running 
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)
```

### *Using break to Exit a Loop*
* **while True** - a loop that starts with *while True* will run forever UNLESS it reaches a **break** statement
* **break** - by calling a break statement, the program will end as soon as the condition is met
  * *break* statements can be used in any of Python's loops, including a *for* loop you want to quit
    that's working through a list or a dictionary
```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        break   # breaks out of the loop when the condition IF city == "quit"
    else:
        print(f"I'd love to go to {city.title()}!")
```
### *Using continue in a Loop*
* **continue** - a control flow statement used within loops (*for* & *while* loops) to skip the rest of the current iteration
                and proceed to the next iteration of the loop
  * Common Use Cases for *continue*: 
    * Skipping invalid or unwanted data
    * Handling error cases
    * Improving code readability
```python
current_number = 0
while current_number < 10:
    current_number += 1 # current_number = current_number + 1 - increment
    if current_number % 2 == 0:
        continue

    print(current_number)
```

## Using a while Loop with Lists & Dictionaries
* To modify a list as you work through it, use a *while* loop
  * Using *while* loops with lists & dictionaries allows you to collect, store, and organize lots of input to examine
    and report on later
```python
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### *Removing All Instances of Specific Values from a List*
```python
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# while loop removes all instances of the value specified "cat"
while "cat" in pets:
    pets.remove("cat")

print(pets)
```

### *Filling a Dictionary with User Input*
```python

```