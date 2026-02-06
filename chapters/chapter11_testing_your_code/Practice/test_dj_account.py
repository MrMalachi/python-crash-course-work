import pytest

from dj_account import DJAccount

@pytest.fixture
def dj():
    """A fixture that provides a re-usable instance."""
    dj = DJAccount("weebtrax", 125_000)

    return dj

def test_default_income_increase(dj):
    """Test & verify 'increase_annual_income' method's default amount works."""
    dj.increase_annual_income()
    assert dj.annual_income == 130_000

def test_custom_income_increase(dj):
    """Test & verify 'increase_annual_income' custom amount works."""
    dj.increase_annual_income(100_000)
    assert dj.annual_income == 225_000

