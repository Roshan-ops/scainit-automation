import pytest
from pytest_bdd import scenarios, given, when, then
from pages.signup_page import SignupPage

scenarios('../features/signup.feature')

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@given('the user is on the login page')
def open_login(signup_page):
    signup_page.open_login_page()

@when('the user navigates to the signup page')
def go_to_signup(signup_page):
    signup_page.click_signup()

@when('the user enters valid signup details')
def valid_signup(signup_page):
    signup_page.signup(
        full_name="Roshan Pokharel",
        email="roshan.valid14523@example.com",
        password="Test@1234",
        phone_number="9876543210"
    )

@when('the user enters a temporary email address')
def temp_email_signup(signup_page):
    signup_page.signup(
        full_name="Roshan Pokharel",
        email="testuser@yopmail.com",
        password="Test@1234",
        phone_number="9876543210"
    )

@then('the signup should be successful')
def verify_success(signup_page):
    assert signup_page.signup_successful(), "Signup was not successful!"

@then('a temporary email error should be displayed')
def verify_temp_email_error(signup_page):
    assert signup_page.temp_email_error_visible(), "Temporary email error not shown!"