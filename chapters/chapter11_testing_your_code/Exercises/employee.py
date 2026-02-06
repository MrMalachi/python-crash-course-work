class Employee:
    """Collect information about employees."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store first & last name, and annual salary as instance attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """
        Adds $5,000 to the annual salary by default,
        but also accepts optional raise amount.
        """
        self.annual_salary += raise_amount


