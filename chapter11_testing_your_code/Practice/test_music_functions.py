# A pytest test that checks exact output.

from music_functions import format_track_label

def test_artist_title():
    """Verify that values result in a correct string based on the function."""
    track_title = format_track_label("cloonee", "separated")
    assert track_title == "Cloonee - Separated"

def test_artist_title_bpm():
    """If I pass another argument (bpm), will it pass the test?"""
    track_title = format_track_label(
        "bordertown", "rapture", 124
    )
    assert track_title == "Bordertown - Rapture (Bpm: 124)"
