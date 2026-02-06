party_size = input("How many people are in your dinner group? ")
party_size = int(party_size)

if party_size > 8:
    print("\nApologies, but the wait time will be 15min.")
else:
    print("\nYour table is ready, you will be seated shortly.")

