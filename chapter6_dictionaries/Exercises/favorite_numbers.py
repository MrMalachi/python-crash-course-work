fav_numbers = {
    "dad": [7, 24],
    "mom": [1, 5, 75],
    "elisha": [15, 34, 44],
    "hezekiah": [3, 15],
    "micah": [0, 44],
    }

for person, numbers in fav_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(number)