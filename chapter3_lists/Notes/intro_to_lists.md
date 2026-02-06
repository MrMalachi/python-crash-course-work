# Chapter 3 - Introducing Lists

### Lists 
* List - a list is a collection of items in a particular order, allowing you to store sets of information in one place, 
            whether you have just a few items or millions of items
  * Ex). bicycles = ['trek', 'cannondale', 'redline', 'specialized']
* It's important to make the name of your list plural, such as *letters*, *digits*, or *names*
* Elements - a list consists of elements. To access an element in the list, tell Python the posititon, or **index**, 
              of the item desired
  * Ex). bicycles = ['trek', 'cannondale', 'redline', 'specialized']
         print(bicycles[0]) # when we ask for a single item from a list, Python returns just that element *without* square brackets
    * Ex). bicycles = ['trek', 'cannondale', 'redline', 'specialized']
           print(bicycles[0].title())   # clean, neatly formatted output
* Index Positions Start at 0, Not 1
  * bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    * The first item in the kist has an index of '0'
    * You can get any element in a list by subtracting 1 from its position in the list 
* Last Index Position Starts at -1
  * Imagine if a list contained hundreds of items within it? To make things easier, if you want to access the last item in a list
        without knowing exactly how long the list is, ask for the item at index -1

### Modifying, Adding, and Removing Elements in a List
* Dynamic - most lists you create will be dynamic, 
            meaning you'll build a list and then add & remove elements from it as your program runs its course
  * Ex). motorcycles[0] = "ducati"
         print(motorcycles)
* Append Method (.append()) - the simplest way to add a new item to a list is to use this method. 
                       When you append an item to a list, the new element is added to the *end* of the list
  * Ex). motorcycles.append("honda")
* Insert Method (.insert()) - this method allows you to add a new element at any position in your list
  * Ex). motorcycles.insert(0, "ducati")
    * .insert(index, object)

### Removing Elements from a List
* del statement - if you know the position of the item you want to remove from a list, use the 'del statement'
  * Ex). del motorcycles[0]
* .pop() method - this method removes the last item in a list, but it lets you work with that item after removing it
  * Ex). In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members
  * Ex). popped_motorcycle = motorcycles.pop()
* Simple way to decide whether to use the del statement or .pop() method:
  * **when you want to delete an item from a list and not use that item in any way, use the 'del statement'; 
    if you want to use an item as you remove it, use the .pop() method.**
* .remove() method - removing an item by value
  * Sometimes you won't know the position of the value you want to remove from a list. 
    If you only know the value of the item you want to remove, you use the .remove() method
    * Ex). motorcycles.remove("ducati")
  * *The .remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more thatn once in the list,
     you'll need to use a loop to make sure all occurrences of the value are removed*

### Organizing a List
* .sort() method - this method **permanently** sorts a list alphabetically by default
  * Ex). cars = ["bmw", "audi", "toyota", "subaru"]
         
       cars.sort()
  * Ex). cars = ["bmw", "audi", "toyota", "subaru"]
         
       cars.sort(reverse=True)    # this passes the argument reverse=True to sort the list in unalphabetical order
* sorted Function - **temporarily** sorts a list without affecting the actual order of the list,
                    and can also accept a 'reverse=True' argument
  * Ex). print("\nHere is the sorted list:")
         
       print(sorted(cars))
* .reverse() method - **permanently** reverses the order of a list *chronologically*, not alphabetically
  * Ex). cars = ["bmw", "audi", "toyota", "subaru"]
         
       print(cars)
    
       cars.reverse()
  * You can also revert to the original list order anytime by applying reverse() to the same list a second time
* len() Function - quickly allows you to find the length of a specified list  
  * Ex). cars = ["bmw", "audi", "toyota", "subaru"]
         
       len(cars)
### Avoiding Index Errors When Working with Lists
* IndexError: list index out of range
  * Occurs when Python can't find an item at the index you requested 
