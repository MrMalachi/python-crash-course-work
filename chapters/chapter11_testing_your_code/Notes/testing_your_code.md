# CHAPTER 11 | TESTING YOUR CODE

## Glossary
* **pytest** - a Python testing framework that can be used to write various types of software tests
* **Third-Party Package** - a library that's developed outside the core Python language
* **pip (pip install packages)** - a package manager tool used to install third-party packages from external resources
* **-- upgrade** - a flag used in a command-line argument used in various software tools (like pip, Helm, and uv) to update
  packages or software releases to their newest available versions
* **-- user** - a flag used in a command-line option, most commonly used with Python's pip installer, that instructs the
  program to install packages or execute actions only for the current user, rather than system-wide
* **Unit Test** - verifies that one specific aspect of a function's behavior is correct
* **Test Case** - a collection of _unit tests_ that together, prove that a function behaves as it's supposed to, within the
  full range of situations (corner cases) you expect it to handle
* **Full Coverage** - includes a full range of unit tests covering all the possible ways you can use a function
* **Assertion** - `assert` is a claim about a condition 
* **Fixture** - a function used primarily within the pytest testing framework to provide a defined, reliable, and
                consistent environment (a fixed baseline) for tests to run
* **Decorator** - a directive placed just before a function definition

## Installing pytest with pip
* 3rd-party packages (libraries outside the core Python language) are kept out of the standard library so they can be
  developed on a timeline independent of the language itself

### *Updating pip*
```commandline
python -m pip install --upgrade pip   
```
* `python -m pip` - tells Python to run the module `pip`
* `install --upgrade` - tells pip to update a package that's already been installed
* `pip` - specifies which third-party package should be updated 


* You can use the following command to update any third-party package installed on your system: 
```shell
$ python -m pip install --upgrade package_name 
``` 

### *Installing pytest*
* -- upgrade - a flag used in a command-line argument used in various software tools (like pip, Helm, and uv) to update
  packages or software releases to their newest available versions
* -- user - a flag used in a command-line option, most commonly used with Python's pip installer, that instructs the
  program to install packages or execute actions only for the current user, rather than system-wide
* Python command to install many third-party packages:
  
  * `$ python -m pip install --user package_name`

## Testing a Function
**name_function.py**
```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

* Check that the program works by using importing the function from the module 'name_function.py'

**names.py**
```python
from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    first = input("\nPlease enter a first name: ")
    if first == "q":
        break
    last = input("\nPlease enter a last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
```

* pytest provides an efficient way to automate the testing of a function's output

### *Unit Tests and Test Cases*
* Unit Test - verifies that one specific aspect of a function's behavior is correct
* Test Case - a collection of _unit tests_ that together, prove that a function behaves as it's supposed to, within the
  full range of situations (corner cases) you expect it to handle
* It's often good enough to write tests for your code's critical behaviors and then aim for full coverage only if the 
  project starts to see widespread use

### *A Passing Test*
* With `pytest` we'll be able to write a single test function. The test function will call the function we're testing, 
  and we'll make an assertion about the value that's returned. If our assertion is correct, the test will pass; 
  if the assertion is incorrect, the test will fail

**Conventions:**
1. The name of a test file is important; it must start with `test_`
   1. Any function that starts with `test_` will be _discovered_ by `pytest` and will be run as part of the testing 
       process
2. Test names should be longer and more descriptive than a typical function name. You'll never call the function
  yourself; `pytest` will find the function and run it for you
3. Make an `assertion`; an _assertion_ is a claim about a condition

**test_name_function.py**
```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Malachi Brown' work?"""
    formatted_name = get_formatted_name("malachi", "brown")
    assert formatted_name == "Malachi Brown"
```

### *Running a Test*
* To run a test, enter the following command into the command-line window:
  * `$ pytest`

```shell
(.venv) malachibrown@Malachis-iMac chapter11_testing_your_code % pytest
=============================================================================== test session starts ===============================================================================
platform darwin -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/malachibrown/Documents/python_work/chapter11_testing_your_code
collected 1 item                                                                                                                                                                  

test_name_function.py .                                                                                                                                                     [100%]

================================================================================ 1 passed in 0.00s ================================================================================
```

### *A Failing Test*
* If a test fails, an output is a single `F`, which tells us that one test failed
* An angle bracket `>` indicates the line of code that caused the failure

```shell
(.venv) malachibrown@Malachis-iMac chapter11_testing_your_code % pytest
=========================================================================================================================== test session starts ===========================================================================================================================
platform darwin -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/malachibrown/Documents/python_work/chapter11_testing_your_code
collected 1 item                                                                                                                                                                                                                                                          

test_name_function.py F                                                                                                                                                                                                                                             [100%]

================================================================================================================================ FAILURES =================================================================================================================================
__________________________________________________________________________________________________________________________ test_first_last_name ___________________________________________________________________________________________________________________________

    def test_first_last_name():
        """Do names like 'Malachi Brown' work?"""
>       formatted_name = get_formatted_name("malachi", "brown")
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: get_formatted_name() missing 1 required positional argument: 'last'

test_name_function.py:5: TypeError
========================================================================================================================= short test summary info =========================================================================================================================
FAILED test_name_function.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last'
============================================================================================================================ 1 failed in 0.02s ============================================================================================================================
```

### *Responding to a Failed Test*
* When a test fails, DO NOT focus on changing the test. If you do, your test might pass, but any code that calls your
  function like the test dies will suddenly stop working
* When a test fails, DO  fix the code that's causing the test to fail by examining the changes you just made to the
  function, and figure out how those changes broke the desired behavior 

**name_function.py**
```python
def get_formatted_name(first, last, middle=""):
    """
    Generate a neatly formatted full name. Make the middle name param. optional
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
```

### *Adding New Tests*
* Now that we know `get_formatted_name()` works for simple names again, let's write a second test for people who include
  a middle name
* We do this by adding another test function to the file _test_name_function_

**test_name_function.py**

```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Malachi Brown' work?"""
    formatted_name = get_formatted_name("malachi", "brown")
    assert formatted_name == "Malachi Brown"

def test_first_last_middle_name():
    """Do names like 'Malachi Nathaniel Brown' work?"""
    formatted_name = get_formatted_name(
        "malachi", "brown", "nathaniel"
    )
    assert formatted_name == "Malachi Nathaniel Brown"
```

## Testing a Class

### *A Variety of Assertions*
* Remember! - an _assertion_ is a claim about a condition, and so far, we've seen just one kind:
  * a claim that a string has a specific value
* The chart below contain examples; anything that can be express as a conditional statement can be included in a test:

**Assertion Statements**

| Assertion                   | Claim                                    |
|-----------------------------|------------------------------------------|
| `assert a == b`             | Assert that two values are equal.        |
| `assert a != b`             | Assert that two values are not equal.    |
| `assert a`                  | Assert that a evaluates to `True`.       |
| `assert not a`              | Assert a evaluates to `False`            |
| `assert element in list`    | Assert that an element is in a list.     |
| `asser element not in list` | Assert that an element is not in a list. |

### *A Class to Test*
* Testing a class is similar to testing a function because much of the work involves testing the behavior of the methods 
  in the class
* The class below helps administer anonymous surveys:

**survey.py**
```python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

* The program below uses the class to demonstrate that `AnonymousSurvey` works:

**language_survey.py**
```python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store the responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
```

* If we want to improve 'AnonymousSurvey' by implementing changes like: 
  * Allow each user to enter more than one response by writing a method to list only unique responses and to report
    how many times each response was given
* While trying to allow each user to enter multiple responses, we could accidentally change how single responses are
  handled
* To ensure we don't break existing behavior as we develop this module, we can write tests for the class

### *Testing the AnonymousSurvey Class*
* Write a test that verifies one aspect of the way 'AnonymousSurvey' behaves
  * Verify that a single response to the survey question is stored properly

**test_survey.py**
```python
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")

    assert "English" in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did your first learn?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Spanish", "Japanese"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

### *Using Fixtures*
* Creating a new instance of a class in each test function is very redundant, so using a _fixture_ helps with code
  reusability
* Below is a fixture being used to create a single survey instance that can be used in both test functions in 
  'test_survey.py'

**test_survey.py**
```python
# Import pytest since we're using a decorator that's defined in pytest.
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():  # Builds an object & returns the new survey.
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)

    return language_survey


def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ["English", "Spanish", "Japanese"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

* Just know that when you've written enough tests that the repetition is getting in the way, there's a well-established 
  way to deal with repetition by using fixtures
* Also, fixtures in simple examples like previously, don't really make the code any shorter or simpler to follow. But in
  projects with many tests, or situations where it takes many lines to build a resource that's used in multiple tests,
  fixtures can drastically improve your test code
* When you want to write a fixture, write a function that generates the resource that's used by multiple test functions.
  Add the `@pytest.fixture` decorator to the new function, and add the name of this function as a parameter for each
  test function that uses this resource