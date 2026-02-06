# This program converts minutes.seconds into seconds.

def get_minutes():
    """Prompt user for the length of minutes in a song & return an integer."""
    minutes = int(input("How many minutes are in the track? "))

    return minutes

def get_seconds():
    """Prompt the user for the length of seconds & return an integer."""
    seconds = int(input("How many seconds are in the track? "))

    return seconds

def convert_time(minutes, seconds):
    """Converts the minutes and seconds into only seconds and returns it."""
    converted_time = (minutes * 60) + seconds

    return converted_time

def display_time(minutes, seconds, total_seconds):
    """Displays a nicely formatted song length converted to seconds."""
    print(
        f"Track length: {minutes}:{seconds:02d}"
        f"\nTrack length in seconds: {total_seconds}"
    )

def run_time_converter():
    """Function orchestrator."""
    minutes = get_minutes()
    seconds = get_seconds()
    total_seconds = convert_time(minutes, seconds)
    display_time(minutes, seconds, total_seconds)

run_time_converter()