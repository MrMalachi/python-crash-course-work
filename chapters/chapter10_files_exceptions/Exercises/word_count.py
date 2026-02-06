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
