import pytest
from apps.ui.workflows.auth_workflow import AuthWorkflow
from data.factories.user_factory import UserFactory


@pytest.mark.e2e
@pytest.mark.signup
@pytest.mark.login
def test_user_can_signup_verify_otp_and_login_with_same_user(page):
    workflow = AuthWorkflow(page)
    user = UserFactory.valid_user()
    workflow.signup_and_login_with_same_user(user)