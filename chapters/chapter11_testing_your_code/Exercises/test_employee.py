import pytest

from employee import Employee

@pytest.fixture
def employee():
    """
    A fixture that will be available to all test functions,
    so a new employee instance does not need to be created in each test func.
    """
    poop = Employee(
        "malachi", "brown", 85_000
    )
    return poop


def test_give_default_raise(employee):
    """Test the 'give_raise' method to verify default raise amount works."""
    employee.give_raise()
    assert employee.annual_salary == 90_000

def test_give_custom_raise(employee):
    """Test the 'give_raise' method to verify a custom raise amount works."""
    employee.give_raise(10_000)
    assert employee.annual_salary == 95_000


