from json import JSONDecodeError
from pathlib import Path
import json

def load_expenses():
    """
    Tries to open expenses.json and load it.
    If file does NOT exist, handle possible exceptions & return an empty list.
    """
    path = Path("expenses.json")

    try:
        read_contents = path.read_text()
        return json.loads(read_contents)
    except FileNotFoundError:
        print(f"{path} does not exist. Creating file now...")
        path.write_text(json.dumps([]))
        return []
    except JSONDecodeError:
        print(f"{path} is empty or corrupted. Resetting file...")
        path.write_text(json.dumps([]))
        return []
    finally:
        print("Finished loading your expenses.")

def get_expense():
    """
    Prompts the user for expenses: item name & cost. And returns a dictionary.
    """
    item = input("Enter an expense item (or 'q' to quit): ").strip()

    if item == "q":
        print("Goodbye!")
        return None

    while True:
        try:
            cost = float(input("Enter the cost: "))
            if cost < 0:
                raise ValueError
        except ValueError:
            print(f"Cost must be a positive number. Try again...")
        else:
            print("Saved!")
            return {"item": item, "cost": cost}

def save_expenses(expense_list):
    """Convert list to json format & write to the expenses.json file."""
    path = Path("expenses.json")
    contents = json.dumps(expense_list)
    path.write_text(contents)

def show_summary(expense_list):
    """Display a summary of saved expenses."""
    if not expense_list:
        print("No expenses recorded yet.")
        return

    total_spent = 0

    for expense in expense_list:
        total_spent += expense["cost"]

    most_recent = expense_list[-1]

    print(f"You have {len(expense_list)} expenses saved.")
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Most recent: {most_recent['item']} - ${most_recent['cost']:.2f}")











