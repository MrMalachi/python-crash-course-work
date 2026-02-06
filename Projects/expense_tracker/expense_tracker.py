"""
Expense Tracker - This program tracks my monthly expenses by:
- Allowing user to input each expense
- Writes specified expenses to a JSON file or creates one if it does not exist
- Allows user to view their expenses by deserializing JSON file and printing
"""
from json import JSONDecodeError
# Import modules & packages to work with functions.
from pathlib import Path
import json
import subprocess

# Global scope to minimize redundancy & maximize reusability within functions.
path = Path("expenses_january_2026.json")

def open_expense_journal(path):
    """
    Opens expense journal or creates one if it does not already exist & returns.
    """
    if path.exists():   # If the file exists, read/loads contents
        contents = path.read_text()
        json.loads(contents)
    else:   # Otherwise, notify user it doesn't exist & create it (empty dict.).
        print(f"{path} does not exist yet. Creating now...")
        contents = json.dumps({})
        path.write_text(contents)

    # Open a file in pycharm from with in a Python script.
        # (Open directly in current PyCharm instance).
    subprocess.run(["pycharm", path])

    return contents # Return the contents of the file (dictionary).

def expense_journal_entry(expense_journal):
    """Prompt user for expenses & return them."""

    while True:
        try:
            expense_price = float(input("\nExpense Price: $"))
            expense_category = input("Expense Category: ").lower().strip()
            expense_item = input("Expense Item: ").lower().strip()

            choice = input(
                "\nWould you like to enter another expense (yes/no)? "
            ).lower()
            if choice == "no":
                return expense_price, expense_category, expense_item
        except ValueError:
            print("\nThe price you enter must be a number. Please try again...")

def convert_expenses_to_dict(price, category, item):
    """Converts raw input strings into a structured dictionary."""
    return {'expense_price': price,
            'expense_category': category,
            'expense_item': item
    }

def save_expense_journal_entry(expenses):
    """Save expense(s) (dictionary) to the JSON file."""



def run_expense_tracker():
    """Orchestrator function."""
    expense_journal = open_expense_journal(path)
    price, category, item = expense_journal_entry(expense_journal)
    converted_expenses = convert_expenses_to_dict(price, category, item)
    save_expense_journal_entry(converted_expenses)

run_expense_tracker()
