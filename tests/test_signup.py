import pytest
from pages.signup_page import SignupPage
from utils.excel_reader import read_signup_test_data

signup_test_data = read_signup_test_data("data/signup_data.xlsx")


@pytest.mark.smoke
def test_user_can_navigate_to_signup_page(page):
    signup_page = SignupPage(page)
    signup_page.open_login_page()
    signup_page.click_signup()

    assert signup_page.is_register_page_visible()

@pytest.mark.regression
@pytest.mark.parametrize("test_data", signup_test_data)
def test_signup_with_valid_details_data_driven(page, test_data):
    signup_page = SignupPage(page)
    signup_page.open_login_page()
    signup_page.click_signup()

    signup_page.signup(
        full_name=test_data["FullName"],
        email=test_data["Email"],
        password=test_data["Password"],
        phone_number=str(test_data["Phone number"])
    )

    assert signup_page.signup_successful()

@pytest.mark.regression
def test_signup_rejects_temporary_email(page):

    signup_page = SignupPage(page)
    signup_page.open_login_page()
    signup_page.click_signup()

    signup_page.signup(
        full_name="Roshan Pokharel",
        email="testuser@yopmail.com",
        password="Test@1234",
        phone_number="9876543210"
    )

    assert signup_page.temp_email_error_visible()