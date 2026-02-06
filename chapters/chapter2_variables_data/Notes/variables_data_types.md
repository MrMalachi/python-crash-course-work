# Chapter 2 - Variables & Data Types

### Python Interpreter
* Interpreter - translates Python code for the computer to understand
* Traceback - a record of where the interpreter ran into trouble when trying to execute your code

### Errors
* NameError - Python can't find identify the variable name provided
  1. Usually because we forget to set the variable's value before using it OR
  2. Because we made a spelling mistake when entering the variable's name
* SyntaxError - occurs when Python doesn't recognize a section of your program as valid code
  * Least specific kind of error, so they can be difficult to identify & correct

### Variables
* Variable - references a certain value 
* To update the new value of a variable, either reassign it to the original variable OR assign it to a new variable
  * Ex). nostarch_url = "https://nostarch.com"
         nostarch_url.removeprefix("https://")
         nostarch_url = nostarch_url.removeprefix("https://")
  * Ex). simple_url = nostarch_url.removeprefix("https://")
* When initializing variables, you can assign values to more than one variable using just a single line of code
  * Ex). x, y, z = 0, 0, 0
* Constants - a constant is a variable whose value stays the same throughout the entire life of a program
  * Ex). MAX_CONNECTIONS = 5000

### Methods 
* Method - an action that Python can perform on a piece of data 
  * Ex). print(name.title())
    * The dot (.) after *name* in name.title() tells Python to make the title() method act on the variable *name*
  * Every method is followed by a set of parentheses, because methods often need additional information to do their work
    That information is provided inside the parentheses
  * lower() - particularly useful for storing data because you typically won't want to trust the capitalization that 
              the users provide, so best practice is to convert strings to lowercase before storing them 
  * upper() - capitalizes every letter in a string

### Data Types
* 
* str - a series of characters within a set of parentheses 
  * f-strings - Python formats the string by replacing the name of any variable in braces with its value.
* floats (float) - any number with a decimal point
* integers (int) - 
* Underscores in Numbers - when writing long numbers, you can group digits using underscores to make large numbers more readable
  * Ex). universe_age = 14_000_000_000
* When you print a number that was defined using underscores, Python prints only the digits
  * Ex). print(universe_age)
         14000000000


### Whitespace
* Whitespace - refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols
  * You can use whitespace to organize your output so it's easier for users to read
* \t - tab
  * Ex). print("\tPython")
* \n - newline 
  * Ex). print("Languages: \nPython\nC\nJavaScript")
* .strip() - a method that removes the whitespace at both the right & left sides of a string, most often used to clean up user input before it's stored in a program
  * To remove the whitespace from the string **permanently**, you have to associate the stripped value with the variable name:
    * Ex). >>> favorite_language = ' python '
               favorite_language = 'python '
               favorite_language = favorite_language.rstrip()
               favorite_language
* .removeprefix() - a method that removes a prefix from a string by entering the prefix you want to remove from the original string
  * Ex). >>> nostarch_url = 'https:/nostarch.com'
             nostarch_url.removeprefix('https://')
             'https:/nostarch.com'

### Numbers
* Integers - you can add, subtract, multiply, and divide integers in Python
  * Exponents - represented by two asteriks (**), followed by the exponent number
* Order of Operations - Python also supports the order of operations (P.E.M.D.A.S.)