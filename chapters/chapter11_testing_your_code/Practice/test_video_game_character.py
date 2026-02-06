import pytest

from video_game_character import GameCharacter

@pytest.fixture()
def character():
    """Return a GameCharacter instance for testing by using a fixture."""
    character = GameCharacter("yoda", 100)
    return character

def test_default_xp_gain(character):   # Pass the fixture 'player' as a parameter.
    """Test the method to verify the default XP increase works."""
    character.increase_xp()
    assert character.current_xp == 200

def test_custom_xp_gain(character):    # Pass the fixture 'player' as a parameter.
    """Test the method to verify a custom XP increase works."""
    character.increase_xp(9_000)
    assert character.current_xp == 9_100

def test_increase_xp_twice(character): # Pass the fixture 'player' as a parameter.
    """Test by calling the method x2 to verify the value increases twice."""
    character.increase_xp()
    character.increase_xp()
    assert character.current_xp == 300
