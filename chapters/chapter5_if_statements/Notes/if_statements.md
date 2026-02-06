# Chapter 5 - If-Statements

## Conditional Tests
* Conditional Test - an expression that can be evaluated as True or False
  * Python uses the values True and False to decide whether the code in an if-statement should be executed 
  
  ### *Checking for Equality*
* Equality Operator (==)
  ### *Checking for Inequality*
* Inequality Operator (!=)
  ### *Numerical/Mathematical Comparisons*
* Less Than, less than or equal to, greater than, and greater than or equal to (<, <=, >, >=)

  ### *Using "or" to Check Multiple Conditions*
* 'and' keyword, both conditions must be met to evaluate to True
  * age_0 >= 21 and age_1 >= 21
  ### *Using "or" to Check Multiple Conditions*
* 'or' keyword, only one condition must be met to evaluate to True
  * age_0 >= 21 or age_1 >= 21
  ### *Checking Whether a Value Is in a List*
  * ex). "mushrooms" in requested_toppings
  ### *Checking Whether a Value Is Not in a List*
  * ex). if user not in banned_users:
  ### *Boolean Expressions*
* Boolean Expression - another name for a conditional test, a Boolean Value is either True or False just like the value of a conditional expression after it has been evaluated 

## if Statements 

* if Statements - a conditional test 
  * ex). if conditional_test:
  
      do something 
* if-else Statements - use this conditional test if you want to take one action when a conditional test passes, and a different action in all other cases
* if-elif-else Chain - use this when you need to test more than two possible situations
  * Python executes only **one** block in this chain. It runs each conditional test **in order**, until one passes
* **Testing Multiple Conditions**
  * **if** more than one block of code needs to run, use a series of independent *if* statements
  * **if** you want only one block of code to run(execute) use an *if-elif-else* chain

## Using if Statements with Lists
* ex). [View toppings.py](../toppings.py)
  * Checks for a special item
  * Checks that a list is *not* empty
    * when the name of a list is used in an if-statement, Python returns True if the list contains at least one item; an empty list evaluates to False
  * Using multiple lists 

