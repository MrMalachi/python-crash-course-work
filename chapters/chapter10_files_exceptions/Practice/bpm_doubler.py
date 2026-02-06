# This program asks for a BPM and shows what double-time would be.

def get_bpm():
    """
    Prompt for BPM & return an integer.
    Use exception handling to deal with errors.
    """
    while True:
        try:
            bpm = int(input("Enter a BPM: "))
            if bpm <= 0:
                raise ValueError
        except ValueError:
            print("BPM must be a positive whole number. Please try again...")
        else:
            return bpm

def double_bpm(bpm):
    """Return BPM doubled."""
    bpm_doubled = bpm * 2

    return bpm_doubled

def show_bpm(original, doubled):
    """Display both the original and doubled BPM."""
    print(f"\nOriginal BPM: {original}\nDouble-Time BPM: {doubled}")

def run_bpm_tool():
    """Orchestrator function."""
    bpm = get_bpm()
    double_time = double_bpm(bpm)
    show_bpm(bpm, double_time)

run_bpm_tool()