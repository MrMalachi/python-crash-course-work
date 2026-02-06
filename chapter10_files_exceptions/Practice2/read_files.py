from pathlib import Path

files = ["notes.txt", "todo.txt", "missing.txt"]

# For every file in the list, create an instance. Try to read the contents of
# the file, and if there is no file, write a user-friendly error message.
# Otherwise, if the file(s) does exist, display its contents.
def reading_multiple_files(files):  # Pass the file list as a parameter.
    """
    Attempt to read each file from a list.
    If a file does not exist, handle the exception and create it.
    """
    for file in files:
        path = Path(file)

        try:
            contents = path.read_text()
        except FileNotFoundError:
            print(f"{file} could not be found. Creating it now...")
            path.write_text("") # If the file does NOT exist, create it.
        else:
            print(contents)

# Call the function and pass the list 'files' as an argument, so the function
# does not have to depend on the global variable 'files'.
reading_multiple_files(files)





