from pathlib import Path

file_names = ["cats.txt", "dogs.txt"]


for file_name in file_names:
    path = Path(file_name)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\n{contents}")








