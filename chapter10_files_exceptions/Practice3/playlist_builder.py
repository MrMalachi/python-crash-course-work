"""
Add tracks to a playlist, show existing playlist count + last track added, and
prevent duplicates.
"""
from json import JSONDecodeError
from pathlib import Path
import json

path = Path("playlist.json")

def load_playlist():
    """Return a list(empty or not)."""
    try:
        contents = path.read_text()
        return json.loads(contents)
    except (FileNotFoundError, JSONDecodeError):
        print("File/Contents does not exist yet. Creating it now...")
        return []

def add_track(playlist):
    """Prompt user to add a track to the playlist. Append to the list."""
    while True:
        track = input(
            "Add a track by typing the track name (or type 'q' to quit): "
        )
        if track.lower() == "q":
            break

        if track in playlist:
            print("That track is already in the playlist!")
        else:
            playlist.append(track)

def save_playlist(playlist):
    """Writes JSON."""
    contents = json.dumps(playlist)
    path.write_text(contents)

def print_playlist(new_track, playlist):
    """Display the added tracks + entire playlist."""
    for new_track in playlist:
        print(f"Added Tracks: \n- {new_track}")

    for track in playlist:
        print(f"\n- {track}")

def run_playlist_builder():
    """Function orchestrator."""
    playlist = load_playlist()
    new_song = add_track(playlist)
    save_playlist(playlist)
    print_playlist(new_song, playlist)



run_playlist_builder()