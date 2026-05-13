from apps.ui.pages.auth.login_page import LoginPage
from apps.ui.pages.auth.signup_page import SignupPage
from domain.models.user import User
from utils.config import Config


class AuthWorkflow:
    def __init__(self, page):
        self.login_page = LoginPage(page)
        self.signup_page = SignupPage(page)

    # LOGIN
    def navigate_to_login_page(self):
        self.login_page.navigate()

    def login_with_credentials(self, email: str, password: str):
        self.login_page.login(email, password)

    def verify_dashboard_visible(self):
        assert self.login_page.dashboard_visible()

    def verify_login_error_visible(self):
        assert self.login_page.error_visible()

    # SIGNUP
    def navigate_to_signup_page(self):
        self.signup_page.open_login_page()
        self.signup_page.click_signup()
        assert self.signup_page.is_register_page_visible(), "Signup page did not load."

    def enter_signup_details(self, user: User):
        self.signup_page.enter_full_name(user.full_name)
        self.signup_page.enter_email(user.email)
        self.signup_page.enter_password(user.password)
        self.signup_page.enter_phone_number(user.phone)

    def submit_signup(self):
        self.signup_page.click_get_started()

    def verify_get_started_disabled(self):
        assert self.signup_page.is_get_started_disabled(), "Button should be disabled."

    def verify_get_started_enabled(self):
        assert self.signup_page.is_get_started_enabled(), "Button should be enabled."

    def verify_otp_page_visible(self):
        assert self.signup_page.is_otp_page_visible(), "OTP page is not visible."

    def verify_email_validation(self):
        assert self.signup_page.is_email_error_visible(), "Email validation error missing."

    def verify_password_validation(self):
        assert self.signup_page.is_password_error_visible(), "Password validation error missing."

    def verify_phone_validation(self):
        assert self.signup_page.is_phone_error_visible(), "Phone validation error missing."

    def verify_temp_email_validation(self):
        assert self.signup_page.is_temp_email_error_visible(), "Temporary email error missing."

    # SIGNUP + OTP + LOGIN E2E
    def complete_signup_with_otp(self, user: User):
        self.navigate_to_signup_page()
        self.enter_signup_details(user)
        self.submit_signup()
        self.verify_otp_page_visible()
        self.enter_fixed_otp()
        self.verify_login_page_visible()

    def enter_fixed_otp(self):
        if not Config.FIXED_OTP:
            raise ValueError("FIXED_OTP is missing. Set it in config/qa.env to complete OTP verification.")

        self.signup_page.enter_otp(Config.FIXED_OTP)
        self.signup_page.click_verify_otp()

    def verify_login_page_visible(self):
        assert self.signup_page.is_login_page_visible(), "Login page is not visible after OTP verification."

    def signup_and_login_with_same_user(self, user: User):
        self.complete_signup_with_otp(user)
        self.login_with_credentials(user.email, user.password)
        self.verify_dashboard_visible()
