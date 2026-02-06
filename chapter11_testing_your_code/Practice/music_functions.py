# A module designed to be used by 'test_music_functions.py'

def format_track_label(artist, title, bpm=None):
    """Returns a neatly formatted string."""
    formatted_track = f"{artist} - {title}"

    if bpm:
        formatted_track += f" (BPM: {bpm})"

    return formatted_track.title().strip()

