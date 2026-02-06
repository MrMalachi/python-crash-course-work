# This program determines the energy level of a DJ set based on the BPM.



def get_bpm():
    """Prompt user for BPM of track & return input as an int."""
    while True:
        try:
            bpm = int(input("What is the BPM of the track? "))
            if bpm <= 0:
                raise ValueError
        except ValueError:
            print("The BPM must be a positive whole number. Please try again...")
        else:
            return bpm

def classify_energy(bpm):
    """Classify the energy and return specified energy level."""
    if bpm <= 90:
        return "Chill"
    elif bpm <= 115:
        return "Mid-Temp/Groove"
    elif bpm <= 130:
        return "Dance/Club Core"
    elif bpm <= 150:
        return "High-Energy Dance"
    else:
        return "Extreme/Hardcore"

def display_energy(bpm, energy_level):
    """Display the energy level to the user, neatly formatted."""
    print(
        f"\nBPM: {bpm}"
        f"\nEnergy Level: {energy_level}"
    )

def run_energy_checker():
    """Orchestrator function."""
    bpm = get_bpm()
    energy_level = classify_energy(bpm)
    display_energy(bpm, energy_level)

run_energy_checker()

