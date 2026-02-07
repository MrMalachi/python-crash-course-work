# import the function from the random module
from random import choice

class TrackSelector:
    """Simulates a DJ software randomly selecting tracks for warm-up sets."""

    # A class attribute for fixed value (in this case, a list).
    tracks_list = [
        "just forget",
        "nightshift",
        "hiizuru style",
        "the stroll",
        "death wish",
        "set it off",
        "the million way of drum",
        "a space in air space in air[interlude]",
        "sanctuary ship",
        "haiku[interlude]",
    ]

    def __init__(self):
        """Initialize attributes."""
        self.playlist = []

    def warmup_playlist(self):
        """
        Randomly selects 4 tracks from track_list to create a warm-up playlist.
        """
        self.playlist = []

        for _ in range(4):
            random_selection = choice(self.tracks_list)
            self.playlist.append(random_selection)

# Create an instance and assign it to the object
playlist1 = TrackSelector()

# Call the method on the object
playlist1.warmup_playlist()

# Print the 4 randomly generated warm-up playlist tracks in a clean format.
print(f"Warm-up Playlist:")

for track in playlist1.playlist:
    print(f"- {track.title()}")



