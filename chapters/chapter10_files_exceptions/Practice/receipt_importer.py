from pathlib import Path

receipts = ["target.txt", "walmart.txt", "costco.txt"]

for receipt in receipts:
    path = Path(receipt)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"\n{receipt}\n{contents}")
