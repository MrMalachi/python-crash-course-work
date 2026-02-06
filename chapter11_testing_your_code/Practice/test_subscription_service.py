import pytest

from subscription_service import SubscriptionPlan

@pytest.fixture()
def plan():
    """Return a Subscriptionplan instance for testing."""
    plan = SubscriptionPlan("silver tier", 10)
    return plan

def test_default_increase_plan_cost(plan):
    """Test the 'increase_plan_cost' method to ensure default increase works."""
    plan.increase_plan_cost()
    assert plan.monthly_cost == 12

def test_custom_increase_plan_cost(plan):
    """Test the 'increase_plan_cost' method to ensure custom increase works."""
    plan.increase_plan_cost(5)
    assert plan.monthly_cost == 15

