import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from utils.config import Config

# Link feature file
scenarios('../features/login.feature')

# Shared fixture
@pytest.fixture
def login_page(page):
    return LoginPage(page)

# Step: Navigate
@given('the user is on the login page')
def navigate_to_login(login_page):
    login_page.navigate()

# Step: Valid login
@when('the user enters valid email and password')
def enter_valid_credentials(login_page):
    login_page.login(Config.EMAIL, Config.PASSWORD)

# Step: Invalid login
@when('the user enters invalid email and password')
def enter_invalid_credentials(login_page):
    login_page.login("wrong@example.com", "wrongpassword")

# Step: Verify dashboard
@then('the user should be redirected to the dashboard')
def verify_dashboard(login_page):
    assert login_page.dashboard_visible(), "Dashboard was not visible after login!"

# Step: Verify error message
@then('an error message should be displayed')
def verify_error(login_page):
    assert login_page.error_visible(), "Error message was not displayed!"