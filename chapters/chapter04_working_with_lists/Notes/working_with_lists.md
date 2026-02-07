# Chapter 4 - Working With Lists

### Looping

  * Loop - a way for the computer to automate repetitive tasks
    * for 
      * ex). magicians = ["alice", "david", "carolina"]
  
           for magician in magicians:
      
           print(magician)
      * Naming conventions in for loops can help you follow the action being done on each item within a for loop.
        Using singular & plural names can help you identify whether a section of code is working with a single element from the list or the entire list.

### Errors

  * IndentationError - occur when people sometimes indent lines of code that don't need to be indented or
    forget to indent line(s) of code that need to be indented
  * LogicalError - when the syntax is valid Python code, but the code does not produce the desired result
    because a problem occurs in its logic

### Functions
* range() function - this function makes it easy to generate a series of numbers, BUT
                     remember the off-by-one behavior
  * ex). for value in range(1, 5):
         
       print(value)
  * ex). for value in range(5):
         
       print(value)
  * range(start, stop, step)
* list() function - if you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function
  * ex). numbers = list(range(1, 6))

       print(numbers)
* min()
* max()
* sum()

### List Comprehensions
* Combines the for loop and the creation of new elements into one line, and automatically appends each new element
  * ex). squares = [value**2 for value in range(1, 11)]

### Working with Part of a List
* **Slicing** - allows you to extract a subsequence (a portion) from a sequence like a list, tuple, or string
  * ex). print(players[:4])
* **Looping Through a Slice** 
  * ex). for player in players[:3]:
* **Copying a List** - omit the first & second index
  * ex). friends_foods = my_foods[:]

### Tuples
* Tuple - a list that cannot change
  * An immutable list is called a *tuple*
  * If you want to define a tuple with 1 element, a trailing comma must be included
    * ex). my_t = (3,)
* Immutable - values that cannot change
* 