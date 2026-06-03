import uuid

import pytest

from pages.login_page import LoginPage
from pages.signup_page import SignupPage


@pytest.mark.smoke
@pytest.mark.regression
def test_registered_user_can_login_with_same_credentials(page):
    password = "Test@1234"
    user = {
        "full_name": "Automation User",
        "email": f"scainit.qa.{uuid.uuid4().hex[:10]}@gmail.com",
        "password": password,
        "phone_number": "9876543210",
    }

    signup_page = SignupPage(page)
    signup_page.open_login_page()
    signup_page.click_signup()
    signup_page.signup(**user)

    assert signup_page.signup_successful()

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(user["email"], user["password"])

    assert login_page.dashboard_visible()
