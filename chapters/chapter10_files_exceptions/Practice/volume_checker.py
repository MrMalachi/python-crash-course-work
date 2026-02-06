# Warn the user if a volume level is too loud.

def get_volume():
    """Prompt user for volume level and return an integer."""
    while True:
        try:
            volume = int(input("Enter a volume level between 0 - 100: "))
            if volume < 0:
                raise ValueError

        except (ValueError, TypeError):
            print("Enter a positive whole number less than or equal to 100.")
        else:
            return volume

def is_safe(volume):
    """Return True or False based of the volume level."""
    if volume >= 66:
        return False
    else:
        return True

def display_warning(volume, safe):
    """Display a warning based on the volume level."""
    print(
        f"\nVolume Level: {volume}"
        f"\nVolume Safe (True or False): {safe}"
    )

def run_volume_checker():
    """Orchestrator function."""
    volume = get_volume()
    safe = is_safe(volume)
    display_warning(volume, safe)

run_volume_checker()