import pytest
from pages.login_page import LoginPage
from utils.config import Config

@pytest.mark.smoke
@pytest.mark.login
def test_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(Config.EMAIL, Config.PASSWORD)

    assert login_page.dashboard_visible()
 
@pytest.mark.regression
@pytest.mark.login
def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong@example.com", "wrongpassword")

    assert login_page.error_visible()