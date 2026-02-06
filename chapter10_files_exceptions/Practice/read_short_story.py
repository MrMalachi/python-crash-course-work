from pathlib import Path

# Create variables to hold two different word counts.
word_count = 0
specific_word_count = 0

# Create an object to store the file path in.
path = Path("short_story.txt")
# Read the entire .txt file and assign the result in a variable called.
contents = path.read_text()
# Use the split() method to break the string of text into a list of substrings.
word_list = contents.split()

# Increase the word_count for every instance of a word in word_list and
# assign this to a more easily read variable.
for word in word_list:
    word_count += 1
total_words = word_count

# Display the total number of words in the .txt file.
print(f"There are {total_words} words in the {path} file.")

# For every instance of the word "the" case-insensitive, increase the counter.
for word in word_list:
    if word.lower() == "the":   # .lower() for comparison.
        specific_word_count += 1

# Display the total number of times the word 'the' appears in the .txt file.
print(f"The word 'the' occurs {specific_word_count} times in the {path} file.")


