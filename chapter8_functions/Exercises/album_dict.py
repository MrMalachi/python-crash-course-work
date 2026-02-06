from zipfile import stringEndArchive64Locator


def make_album(artist, title, tracks=None):
    """Returns a dictionary describing an album."""
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }

    if tracks:  # Key-value pair will be added to dictionary based on condition
        album_dict["tracks"] = int(tracks)

    return album_dict


# Print the called function 'make_album' 3x to display the dictionaries
album = make_album("drake", "nothing was the same")
print(f"Artist: {album["artist"]}\nTitle: {album["title"]}")

album = make_album("baltra", "ted")
print(f"\nArtist: {album["artist"]}\nTitle: {album["title"]}")

album = make_album("braga circuit", "splash", "11")
print(f"\nArtist: {album["artist"]}\nTitle: {album["title"]}\nTracks: {album["tracks"]}")



