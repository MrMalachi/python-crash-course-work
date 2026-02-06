python_glossary = {
    "iteration": "a technique that marks out a block of statements within a "
               "computer program for a defined number of repetitions.",
    "method": "a function that belongs to a class and operates on an object.",
    "dictionary": "a collection of key-value pairs, where each key is "
                    "connected to a value.",
    "list": "a built-in, ordered, and mutable collection of items.",
    "conditional test": "an expression that can be evaluated to as either "
                        "True or False.",
    "variable": "serves as a named storage location for a value.",
    "string": "an immutable sequence of characters used to represent text.",
    "data type": "classify the kind of values variables can hold, "
                 "determining the operations that can be performed on them.",
    "function": "named blocks of reusable code designed to perform specific tasks.",
    "tuple": "an ordered, immutable collection of items.",
    }

print("\nPython Dictionary:\n")
for word, meaning in python_glossary.items():
    print(f"\n\t{word.title()} - {meaning.capitalize()}\n")

"""
# Beginner friendly
word = "iteration"
print(f"\n{word.title()} - {python_glossary["iteration"].capitalize()}")

word = "method"
print(f"\n{word.title()} - {python_glossary["method"].capitalize()}")

word = "dictionary"
print(f"\n{word.title()} - {python_glossary["dictionary"].capitalize()}")

word = "list"
print(f"\n{word.title()} - {python_glossary["list"].capitalize()}")

word = "conditional test"
print(f"\n{word.title()} - {python_glossary["conditional test"].capitalize()}\n")
"""



