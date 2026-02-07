current_number = 0
while current_number < 10:
    current_number += 1 # current_number = current_number + 1 - increment
    if current_number % 2 == 0:
        continue

    print(current_number)

