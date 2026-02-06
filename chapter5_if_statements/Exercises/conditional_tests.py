tea = "jasmine"
print("Is tea == 'jasmine'? I predict True.")
print(tea == "jasmine")

print("\nIs tea == 'assam'? I predict False.")
print(tea == "assam")

print()

music_genre = "house"
print("Is the genre of music == 'pop'? I predict False.")
print(music_genre == "pop")

print("\nIs the genre of music == 'house'? I predict True.")
print(music_genre == "house")

print()

travel_destination = "italy"
print("Is my next travel destination == 'italy?' I predict True.")
print(travel_destination == "italy")

print("\nIs my next travel destination 'japan?' I predict False.")
print(travel_destination == "japan")

print()

favorite_anime = "samurai champloo"
print("Is my favorite anime == 'bleach?' I predict False.")
print(favorite_anime == "bleach")

print("\nIs my favorite anime == 'samurai champloo?' I predict True.")
print(favorite_anime == "samurai champloo")

print()

favorite_number = 4
print("Is my favorite number == 4? I predict True.")
print(favorite_number == 4)

print("\nIs my favorite number == 7? I predict False.")
print(favorite_number == 7)

print()

cologne_brands = ["burberry", "tom ford", "dior sauvage", "jean paul", "versace", "yves saint laurent"]
cologne_owned = "burberry"
cologne_not_owned = "BLEU DE CHANEL"
print(f"Do I own Burberry cologne: True or False?")
if cologne_owned in cologne_brands:
    print(cologne_owned == "burberry")
else:
    print(cologne_owned == "jo malon")

print()

if cologne_not_owned.lower() not in cologne_brands:
    print(f"True or False: I own {cologne_not_owned}?", cologne_not_owned == "burberry")
else:
    print(cologne_owned == "BLEU DE CHANEL")