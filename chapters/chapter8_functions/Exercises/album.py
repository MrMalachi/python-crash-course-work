def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary containing information about an album"""
    album_info = {
        "artist": artist_name.title(),
        "album": album_title.title(),
    }
    if number_of_songs:
        album_info["number of songs"] = number_of_songs
    return album_info

album = []

while True:
    print("\nEnter 'q' at any time to quit.")
    artist_prompt = input("What music artist are you thinking of? ")
    if artist_prompt == "q":
        break

    print("\nEnter 'q' at any time to quit.")
    album_prompt = input(f"What is your favorite {artist_prompt.title()} album? ")
    if album_prompt == "q":
        break

    print("\nEnter 'q' at any time to quit.")
    song_count_prompt = int(input(f"How many songs are in {artist_prompt.title()}'s '{album_prompt.title()}' album? "))
    if artist_prompt == "q":
        break

    album.append(make_album(artist_prompt, album_prompt, song_count_prompt))
    print(album)

print("\nThank you for responding!")


