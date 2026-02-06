class SubscriptionPlan:
    """A class that represents a subscription service."""

    def __init__(self, plan_name, monthly_cost):
        """Store the name and monthly cost of a subscription."""
        self.plan_name = plan_name.title()
        self.monthly_cost = int(monthly_cost)

    def increase_plan_cost(self, increase_amount=2):
        """Increases monthly cost of a subscription plan set to default price."""
        self.monthly_cost += increase_amount



