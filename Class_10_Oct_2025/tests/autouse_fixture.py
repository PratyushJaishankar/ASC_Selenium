import pytest

@pytest.fixture(autouse=True)
def auto_cleanup():
    """Runs automatically before and after EVERY test without being requested"""
    # Setup
    print("\n🔧 AUTO SETUP: Before test")
    yield
    # Teardown
    print("🗑️  AUTO TEARDOWN: After test")

def test_addition():
    print("Running test_addition")
    assert 1 + 1 == 2

def test_subtraction():
    print("Running test_subtraction")
    assert 5 - 3 == 2

def test_multiplication():
    print("Running test_multiplication")
    assert 2 * 3 == 6