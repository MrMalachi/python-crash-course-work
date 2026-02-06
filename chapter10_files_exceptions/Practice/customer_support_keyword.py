from pathlib import Path

path = Path("support_tickets.txt")
contents = path.read_text()
tickets_split = contents.lower().split()
word_repeat = tickets_split.count("refund")

print(f"The word 'refund' appears {word_repeat} times in {path}")

