"""
This program uses functional decomposition to:
- Take a messy song title and display it nicely
"""

def get_title():
    """Prompts for a song title & returns a string."""
    song_title = input("Enter the title of any song: ")

    return song_title

def format_title(title):
    """Returns title-cased version of song title."""
    formatted_song = title.title()

    return formatted_song

def display_title(title):
    """Prints formatted song title."""
    print(f"Formatted Song Title: {title}")

def run_title_formatter():
    """Orchestrates the song title formatting process."""
    title = get_title()
    formatted_title = format_title(title)
    display_title(formatted_title)

run_title_formatter()