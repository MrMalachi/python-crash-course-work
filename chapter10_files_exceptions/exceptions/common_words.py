from pathlib import Path

files = ["meditations.txt", "the_art_of_war.txt", "the_prince.txt"]

for file in files:
    path = Path(file)
    contents = path.read_text()

    words = contents.lower().split()
    number_of_words = len(words)
    print(f"\nThere are {number_of_words} words in {file}.")

    word_count = words.count("the")
    print(f"The word 'the' appears {word_count} times in this book.")


