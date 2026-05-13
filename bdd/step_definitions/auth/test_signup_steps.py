import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from apps.ui.workflows.auth_workflow import AuthWorkflow
from data.factories.user_factory import UserFactory

scenarios("../../features/auth/signup.feature")


@pytest.fixture
def auth_workflow(page):
    return AuthWorkflow(page)


@given("the user is on the signup page")
def user_is_on_signup_page(auth_workflow):
    auth_workflow.navigate_to_signup_page()


@when("the user enters valid signup details")
def user_enters_valid_signup_details(auth_workflow):
    user = UserFactory.valid_user()
    auth_workflow.enter_signup_details(user)


@when("the user clicks on Get Started")
def user_clicks_get_started(auth_workflow):
    auth_workflow.submit_signup()


@when("the user enters a temporary email address")
def user_enters_temp_email(auth_workflow):
    user = UserFactory.user_with_email("testuser@yopmail.com")
    auth_workflow.enter_signup_details(user)
    auth_workflow.submit_signup()


@when(parsers.parse('the user enters signup details with password "{password}"'))
def user_enters_invalid_password(auth_workflow, password):
    user = UserFactory.user_with_password(password)
    auth_workflow.enter_signup_details(user)


@when(parsers.parse('the user enters signup details with phone "{phone}"'))
def user_enters_invalid_phone(auth_workflow, phone):
    user = UserFactory.user_with_phone(phone)
    auth_workflow.enter_signup_details(user)


@then("the Get Started button should be disabled")
def get_started_should_be_disabled(auth_workflow):
    auth_workflow.verify_get_started_disabled()


@then("the Get Started button should be enabled")
def get_started_should_be_enabled(auth_workflow):
    auth_workflow.verify_get_started_enabled()


@then("the OTP page should be displayed")
def otp_page_should_be_displayed(auth_workflow):
    auth_workflow.verify_otp_page_visible()


@then("temporary email validation should be displayed")
def temp_email_validation_should_be_displayed(auth_workflow):
    auth_workflow.verify_temp_email_validation()


@then("password validation should be displayed")
def password_validation_should_be_displayed(auth_workflow):
    auth_workflow.verify_password_validation()


@then("phone validation should be displayed")
def phone_validation_should_be_displayed(auth_workflow):
    auth_workflow.verify_phone_validation()