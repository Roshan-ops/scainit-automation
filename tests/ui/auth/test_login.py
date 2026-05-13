import pytest
from apps.ui.workflows.auth_workflow import AuthWorkflow
from utils.config import Config

@pytest.mark.smoke
@pytest.mark.login
def test_login_with_valid_credentials(page):
    workflow = AuthWorkflow(page)

    workflow.navigate_to_login_page()
    workflow.login_with_credentials(Config.EMAIL, Config.PASSWORD)

    workflow.verify_dashboard_visible()


@pytest.mark.regression
@pytest.mark.login
def test_login_with_invalid_credentials(page):
    workflow = AuthWorkflow(page)

    workflow.navigate_to_login_page()
    workflow.login_with_credentials("wrong@example.com", "wrongpassword")

    workflow.verify_login_error_visible()