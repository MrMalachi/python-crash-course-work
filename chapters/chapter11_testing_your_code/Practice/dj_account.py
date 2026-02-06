class DJAccount:
    """A model for a DJ's annual income."""

    def __init__(self, stage_name, annual_income):
        """Store a DJ's stage name & annual income."""
        self.stage_name = stage_name.title()
        self.annual_income = annual_income

    def increase_annual_income(self, increase_income=5_000):
        """Increases the DJ's annual income (default/custom)."""
        self.annual_income += increase_income

