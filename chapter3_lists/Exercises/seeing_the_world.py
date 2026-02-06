places_to_visit = ["Tokyo", "Rome", "Seoul", "Cairo", "Brazil"]
print(places_to_visit)

print("\nThis is the list temporarily sorted:")
print(sorted(places_to_visit))

print("\nBUT, the list is not sorted permanently:")
print(places_to_visit)

print("\nHere is the list reversed (this method is permanent):")
places_to_visit.reverse()
print(places_to_visit)

print("\nHere is the list back to its original order:")
places_to_visit.reverse()
print(places_to_visit)

print("\nHere is the list sorted alphabetically:")
places_to_visit.sort()
print(places_to_visit)

print("\nHere is the list in reverse-alphabetical order:")
places_to_visit.sort(reverse=True)
print(places_to_visit)