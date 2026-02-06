# CHAPTER 10 | FILES AND EXCEPTIONS

## Glossary
* **Text Files (.txt)** - simple, basic files that store text (letters, numbers, symbols) without any special formatting
                        like bold, italic, colors, or images, making them highly compatible and small in size. 

* **Path** - a *path* is the exact location of a file or folder on a system
* **Pathlib** (`Pathlib`) - path library is a module that makes it easier to work with files and directories,
                          no matter which operating system you or your program's users are working with (*library*)
* **Library** - a module that provides specific functionality 
* **.rstrip()** - a method belonging to the built-in string (str) class, used to remove trailing whitespace characters
* **Method Chaining** - a programming technique that allows multiple methods to be called on the same object in a single,
                        continuous expression
  * Ex). `contents = path.read_text().rstrip()`
* **Relative Path** - tells Python to look for a given location relative to the directory where the currently running
                      program file is stored
  * Ex). `path = Path("reading_from_a_file/pi_digits.txt")`
* **Absolute Path** - tells Python exactly where the file is on your computer, regardless of where the program that's
                      being executed is stored
  * Ex). `/Users/malachibrown/Documents/python_work/chapter10_files_exceptions/reading_from_a_file/pi_digits.txt`
**Directory** - a folder (container or index) that organizes items
* **.splitlines()** - a method that splits a string into a list of lines, returning a list of all the lines in a file
  * Ex). 
    ```python
    s = "A\nB\n"
    result = s.splitlines()
    print(result)
    ```
* **.split()** - a method that splits/breaks a string of text into a list of substrings whenever there is a white space
* **.read_text()** - a method that opens a file and reads its entire content as a string without an explicit 'open()'
* **.write_text()** - a method that allows you to write a string and stores it in a file instead of printing it
  * **Right/Left-Hand Operand (RHO/LHO)** - operands are the values that an operator works on, and their position
                                            relative to the operator defines them as left-hand or right-hand operands
* **Exceptions** - special objects that manage errors that arise during a program's execution
* **Exception Object** - created whenever an error occurs that makes Python unsure of what to do next
* **Traceback** - a report of the exception that was raised during an error (part of an error message)
* **Try-Except Blocks** - handle exceptions that asks Python to do something, but also tells Python what to do if an
                          exception is raised, allowing a program to continue running despite thing going wrong
* **Encoding argument** - an argument that is need when your system's default encoding does not match the encoding 
                          of the file that's being read
  * Ex). `contents = path.read_text(encoding="utf-8")`
* **UTF-8** - Unicode Transformation Format - 8-bit translates text into machine-readable binary
* **pass (`pass`)** - a statement placed within the `except` block that intentionally allows the program to fail 
                      silently without reporting the exception catch to the user
* * **Data Structures** - a specialized format for organizing, storing, and managing data in memory so that it can be accessed
                    and used efficiently (lists or dictionaries)
* **JSON (`json`)** - JavaScript Object Notation is a lightweight, human-readable text format for storing and
                      exchanging data
* **json.dumps()** - a function that takes one argument: a piece of data that should be converted to the JSON format
                     and returns a string
* **json.loads()** - a function from Python's built-in json module that converts a JSON-formatted string into a 
                     corresponding Python object 
* **exists()** - a method that returns `True` if a file or folder exists and `False` if it doesn't
* **Refactoring** - restructuring existing code's internal design to improve readability, maintainability,
                    and structure, WITHOUT changing its external functionality or behavior
* **.json()** - JSON functions only converts between Python objects and strings, they do NOT read or write files
* **Serialize** - convert a Python object to a JSON string

## Reading from a File
* When you want to work with the information in a text file, the first step is to read the file into memory

### *Reading the Contents of a File*

**pi_digits.txt**
```text
3.141592635
  8979323846
  2643383279
```

**file_reader.py**
```python
# import the Path class from the module (library) 'pathlib'.
from pathlib import Path

# Build a Path object representing the file 'pi_digits.txt',
# which we assign to the variable 'path'.
path = Path("pi_digits.txt")
# Use the 'read_text()' method to read the entire contents of the file.
# The contents of the file are returned as a single string,
# which we assign to the variable 'contents'.
contents = path.read_text().rstrip()    # Remove the extra blank line.
# When we print the value of 'contents', we see the entire contents of the .txt
print(contents)
```

### *Relative and Absolute File Paths*
* There are two main ways to specify paths in programming:
  1. _Relative Path_ - shorter because the path is relative to the directory (folder)
  2. _Absolute Path_ - longer because they usually start at your system's root folder

### *Accessing a File's Lines*
* Allows you to rewrite certain information you re looking for in a file by modifying the text in someway

**file_reader.py**
```python
# import the Path class from the module (library) 'pathlib'.
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()   # Assign the list to the variable 'lines'.
for line in lines:
    print(line)
```

### *Working with a File's Contents*
* After you've read the contents of a file into memory, you can do whatever you want with that data

**pi_string.py**
```python
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""  # Create a variable to hold the digits of 'pi'.
for line in lines:  # A loop that adds each line of digits to 'pi_string'.
    pi_string += line.strip()   # Use '.lstrip()' the whitespace that was on
                                # the left side of the digits in each line.
print(pi_string)    # Print the string
print(len(pi_string))   # Print how long the string is (36 characters).
```

### *Large Files: One Million Digits*
* So far, we've analyzed a text file that contains only three lines, but the code in these examples would work just as 
  well on much larger files:

**pi_string.py**
```python
from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""  # Create a variable to hold the digits of 'pi'.
for line in lines:  # A loop that adds each line of digits to 'pi_string'.
    pi_string += line.strip()   # Use '.lstrip()' the whitespace that was on
                                # the left side of the digits in each line.

# Print by slicing from index 0, up to but not including index 52.
print(f"{pi_string[:52]}...")
print(len(pi_string))   # Print how long the string is (36 characters).
```

### *Is Your Birthday Contained in Pi?*
* Express each birthday as a string of digits and seeing if that string appears anywhere in 'pi_string'

**pi_birthday.py**
```python
from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""  # Create a variable to hold the digits of 'pi'.
for line in lines:  # A loop that adds each line of digits to 'pi_string'.
    pi_string += line.strip()

# Prompt for the user's birthday, and then check if that str is in 'pi_string'.
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

## Writing to a File
* When you write to a file, the output will still be available after you close the terminal containing your 
  program's output
* Python can only write strings to a text file
* `write_text()` allows you to write a string to a specified file

### _Writing a Single Line_

**write_message.py**
```python
from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming!")
```

### _Writing Multiple Lines_
* The `write_text()` method does a few things behind the scenes:
  * If the file that `path` points to doesn't exist, it creates that file
  * Also, after writing the string to the file, it makes sure the file is closed properly
    * Files that aren't closed properly can lead to missing or corrupted data (like force ejecting a thumb-drive)
* To write more than one line to a file, you need to build a string containing the entire contents of the file,
  and then call `write_text()` with that string 
* Be careful when calling `write_text()` on a path object:
  * If the file already exists, `write_text()` will erase the current contents of the file and 
    write new contents to the file

**write_message.py**
```python
# Import the Path class from the pathlib library (module).
from pathlib import Path

# Adds the value of the right-hand operand to the left-hand operand and then
# assigns the new result back to the left-hand operand.
# contents = contents + "string"
contents = "I love programming!\n"  # Define variable to hold contents of file.
contents += "I love creating new software programs.\n"
contents += "I also love working with data.\n"

# Create an instance of 'Path'
path = Path("programming.txt")
# Use the write_text() method to write the value of contents to the file.
path.write_text(contents)
```

## Exceptions
* Instead of tracebacks, which can be confusing for users to read, _try-excepts_ blocks allow users to see friendly error messages that you the
  programmer have written

### _Handling the ZeroDivisionError Exception_
* An example of an exception object created from a traceback provided by Python due to an error 

**division_calculator.py**
```python
print(5 / 0)    # Not possible, so Python provides an exception object 
```

### *Using try-expect Blocks*
* When you think an error may occur, you can write a _try-except_ block to handle the exception that might be raised
* You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of
  exception
* Try-Except:
  * If the code inside a try block works, Python skips over the except block.
  * If the code inside a try block causes an error, Python looks for an except block whose error matches the one that was 
    raised, and runs the code in that block

**division_calculator.py**
```python
# If the code inside a try block works, Python skips over the except block.
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### *Using Exceptions to Prevent Crashes* 
* Handling errors is especially important when the program has more work to do after the error occurs
* The following program does nothing to handle errors, 
  so asking it to divide by zero causes it to crash:

**division_calculator.py**
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")    # Prompts user to input a 'first_number'
    if first_number == "q": # If the user DOES NOT enter a 'q' to quit...
        break  
    second_number = input("Second number: ")    # it prompts the user to input a second number.
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number) # Divide these two numbers to get the answer.
print(answer)
```

* In a malicious setting, attackers will learn more than you want them to because of a Traceback. For example,
  they'll know the name of your program file, and they'll see part of your code that isn't working properly, so they 
  can exploit
* Nontechnical users will be confused by Tracebacks

### *The else Block*
* We can make this program more error resistant by wrapping the line that might produce errors in a _try-except_ block
* The only code that should go in a try block is code that might cause an exception to raised
* By anticipating likely sources of errors, your code will be resistant to innocent user mistakes and malicious attacks

**division_calculator.py**
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
```

### *Handling the FileNotFoundError Exception*
* Use a _try-else_ block to handle working with missing files, files you're looking for might be in a different
  location, the filename might be misspelled, or the file might not exist at all
* In the example below, the result is a friendly error message instead of a traceback

**alice.py**
```python
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
```

### *Analyzing Text*
* The split() method is a string method, which by default splits a string whenever it finds any whitespace
* The program `alice.py` below will count and display the approximate number of words in the e-book titled, "Alice's 
  Adventures in Wonderland" from the `alice.txt` path

**alice.py**
```python
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
```

### *Working with Multiple Files*
* In order to analyze more books, we can move the bulk of this program to a function called `count_words()`
* If the `try-except` block was not used in the program below, the user would see a full traceback, and the program 
  would stop running after trying to analyze 'siddhartha.txt'. It would never analyze 
  'moby_dick.txt' or 'little_women.txt'

**word_count.py**
```python
from pathlib import Path

def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# The names of the files are first stored as simple strings.
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt",
              "little_women.txt"]
for file_name in file_names:
    path = Path(file_name)  # Each string is then converted to a 'Path' object.
    count_words(path)   # Call the function and pass it the argument.
```

### *Failing Silently*
* You don't need to report every exception you catch, so the `pass` statement tells Python to do nothing and carry-on
  as if nothing happened 
* The `pass` statement can act as a placeholder, by reminding you that you're choosing to do nothing at a specific
  point in your program's execution and that you might want to do something there later

**word_count.py**
```python
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# The names of the files are first stored as simple strings.
file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt",
              "little_women.txt"]
for file_name in file_names:
    path = Path(file_name)  # Each string is then converted to a 'Path' object.
    count_words(path)   # Call the function and pass it the argument.
```

### *Deciding Which Errors to Report*
* Giving users information they aren't looking for can decrease the usability of your program, and the opposite is true
* Python's error-handling structures give you fine-grained control over how much to share with users when things go
  wrong; it's up to you to decide how much information to share 

## Storing Data
* `json` (JavaScript Object Notation) modules allows you to convert simple Python data structures into JSON-formatted strings, and then load the data
   from that file the next time the program runs 
* THe JSON data format is not specific to Python, so you can share data you store in the JSON format with people
  who work in many other programming languages 

### *Using json.dumps() and json.loads()*
* The program below stores a set of numbers (list):

**number_writer.py**
```python
from pathlib import Path
import json # Import the json module that allows us to convert.

numbers = [2, 3, 5, 7, 11, 13]  # The list we want to convert.

path = Path("numbers.json") # Choose a filename in which to store the list.
contents = json.dumps(numbers)  # Generate a string that is the JSON equivalent
path.write_text(contents)   # Use the method to write to the file.
```

* The program below reads the set of numbers (list) back into memory:

**number_reader.py**
```python
from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)  # Pass the contents of the file to json.loads()
                                # Take a formatted str & return a Python object

print(numbers)  # Display the data shared between two programs
```

### *Saving and Reading User-Generated Data*
* Saving data with `json` is useful when you're working with user-generated data, because if you don't store your user's
  information somehow, you'll lose it when the program stops running

**remember_me.py**
```python
from pathlib import Path
import json

username = input("What is your name? ").title() # Prompt for a username to store

path = Path("username.json")    # Write the data just collected to the file.
contents = json.dumps(username)
path.write_text(contents)

# Inform the user that we've stored their information.
print(f"We'll remember you when you come back, {username}!")
```

* Now, greet the user whose name has already been stored in username.json

**greet_user.py**
```python
from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text() # # Read the contents of the data file
username = json.loads(contents) # Use json.loads() to assign data to variable. 

print(f"Welcome back, {username}!")
```

* Combine both programs so when someone runs `remember_me.py`, we'll retrieve their username from memory if possible;
  if not, we'll prompt for a username and store it in `username.json` for next time

**remember_me.py**
```python
from pathlib import Path
import json

# Whichever block executes, the result is a username and an appropriate greeting

path = Path("username.json")
if path.exists():   # Find out if a username has already been stored (exists).
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What's your name? ").title()
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
```

* Even thought the data in this section is just a single string, the program would work just as well with any data that
  can be converted to a JSON-formatted string

### *Refactoring Pt. 1*
* Often you'll come to a point where your code will work, but you'll recognize that you could improve the code by 
  breaking it up into a series of functions that have specific jobs (_refactoring_)
* Below, we can refactor `remember_me.py` by moving the bulk of its logic into one or more functions because its focus
  on greeting the user

**remember_me.py**
```python
from pathlib import Path
import json

# Whichever block executes, the result is a username and an appropriate greeting
def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    if path.exists():   # Find out if a username has already been stored (exists).
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What's your name? ").title()
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

* `remember_me.py` has been refactored by using a function, but the program is doing more than just greeting the user - 
   it's also retrieving a stored username if one exists and prompting for a new username if one doesn't 

### *Refactoring Pt. 2*
* In the program below, we'll refactor `remember_me.py` so there is more than one function handling multiple tasks

**remember_me.py**
```python
from pathlib import Path
import json

# Whichever block executes, the result is a username and an appropriate greeting
def get_stored_username(path):
    """Greet stored username if available."""
    if path.exists():   # Find out if a username has already been stored (exists).
        contents = path.read_text()
        username = json.loads(contents)
        # A function should either return the value you're expecting or 'None'.
        return username
    else:
        return None

def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What's your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
```

### *Refactoring Pt. 3*
* Remember, _functions_ help implement **Separation of Concerns (SoC)** - a general principle for separating a program 
  into distinct sections, where each section addresses a separate concern
* Refactor `remember_me.py` so that if the username doesn't exist, we should move the code that prompts for a new
  username to a function dedicated to that purpose

**remember_me.py**
```python
from pathlib import Path
import json

# Whichever block executes, the result is a username and an appropriate greeting
def get_stored_username(path):
    """Greet stored username if available."""
    if path.exists():   # Find out if a username has already been stored (exists).
        contents = path.read_text()
        username = json.loads(contents)
        # A function should either return the value you're expecting or 'None'.
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)    # Encapsulate the logic for retrieving a stored username.
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

### Saving and Loading Data with JSON
**Saving Data (Python --> JSON --> file)**
* What you start with: `favorite_number = input("What's your favorite number? ")`

*Step 1:* Convert Python --> JSON text

`contents = json.dumps(favorite_number)`
* json.dumps() serializes a Python object
* Output is a string
* Files can only store text --> this step is REQUIRED

*Step 2:* Write JSON text to file

`path.write_text(contents)`
* You CANNOT write a Python object directly to a file - only text

**Loading Data (file --> JSON --> Python)**
* What you start with: `contents = path.read_text()`

*Step 1:* Convert JSON text --> Python

`favorite_number = json.loads(contents)`
* json.loads() **deserializes** text
* Output is a Python object again
* You must read the file first - there is nothing to convert until you do

**Conclusion: Order Must Be Opposite**
* Saving
  * Python object --> JSON string --> file
* Loading
  * file --> JSON string --> Python object 
