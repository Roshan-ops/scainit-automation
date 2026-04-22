from pages.base_page import BasePage
from utils.config import Config

class SignupPage(BasePage):
    SIGNUP_NAV_BUTTON = "//a[@id='register-link']"

    FULL_NAME_INPUT = '#register-fullname'
    EMAIL_INPUT = '#register-email'
    PASSWORD_INPUT = '#register-password'
    PHONE_INPUT = '#register-phone'
    GET_STARTED_BUTTON = '#register-submit'
    REGISTER_PAGE_IDENTIFIER = '//h2[contains(text(), "Create Free Account")]'
    SUCCESS_ELEMENT = '#success-toast' 
    TEMP_EMAIL_ERROR = '#error-toast'

    def open_login_page(self):
        self.open(f"{Config.BASE_URL}/login")

    def click_signup(self):
        self.click(self.SIGNUP_NAV_BUTTON)

    def is_register_page_visible(self):
        return self.is_visible(self.REGISTER_PAGE_IDENTIFIER, timeout=10000)

    def enter_full_name(self, full_name: str):
        self.fill(self.FULL_NAME_INPUT, full_name)

    def enter_email(self, email: str):
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)

    def enter_phone_number(self, phone_number: str):
        self.fill(self.PHONE_INPUT, phone_number)

    def click_get_started(self):
        self.click(self.GET_STARTED_BUTTON)

    def signup(self, full_name: str, email: str, password: str, phone_number: str):
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_phone_number(phone_number)
        self.click_get_started()

    def signup_successful(self):
        return self.is_visible(self.SUCCESS_ELEMENT, timeout=10000)

    def temp_email_error_visible(self):
        return self.is_visible(self.TEMP_EMAIL_ERROR, timeout=5000)