from pathlib import Path

path = Path("receipt_file.txt")

def read_write_receipt(path):
    """Read the contents of a file. If the file does NOT exist, create it."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
         print(f"{path} not found. Creating it now...")
         path.write_text("")
    else:
        print(contents)
    finally:
        print("Receipt check complete.")

def word_count(path):
    """
    Count how many times a word appears in a file. The function also uses its
    own exception handling so it's not dependent on another function.
    """
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Cannot count words - file does not exist.")
        return 0

    split_contents = contents.lower().split()
    return split_contents.count("the")


# Be sure to pass the path object as an argument for both functions.
# This way, you don't have hidden global variables & the function is reusable.
read_write_receipt(path)





