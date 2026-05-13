from pytest_bdd import scenarios, given, when, then

from apps.ui.workflows.auth_workflow import AuthWorkflow
from utils.config import Config

scenarios("../../features/auth/login.feature")


@given("the user is on the login page")
def user_is_on_login_page(page):
    page.auth_workflow = AuthWorkflow(page)
    page.auth_workflow.navigate_to_login_page()


@when("the user enters valid email and password")
def user_enters_valid_credentials(page):
    page.auth_workflow.login_with_credentials(
        Config.EMAIL,
        Config.PASSWORD
    )


@when("the user enters invalid email and password")
def user_enters_invalid_credentials(page):
    page.auth_workflow.login_with_credentials(
        "wrong@example.com",
        "wrongpassword"
    )


@then("the user should be redirected to the dashboard")
def user_should_be_redirected_to_dashboard(page):
    page.auth_workflow.verify_dashboard_visible()


@then("an error message should be displayed")
def error_message_should_be_displayed(page):
    page.auth_workflow.verify_login_error_visible()