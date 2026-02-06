class GameCharacter:
    """A video-game character earns points (XP) after missions."""

    def __init__(self, name, current_xp):
        """Store a character's name & current XP."""
        self.name = name
        self.current_xp = int(current_xp)

    def increase_xp(self, gain_xp=100):
        """Increases a character's XP by default 100."""
        self.current_xp += int(gain_xp)

