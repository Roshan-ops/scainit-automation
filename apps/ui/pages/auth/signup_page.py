from apps.ui.pages.base.base_page import BasePage
from utils.config import Config

class SignupPage(BasePage):
    SIGNUP_NAV_BUTTON = "//a[@id='register-link']"

    FULL_NAME_INPUT = '#register-fullname'
    EMAIL_INPUT = '#register-email'
    PASSWORD_INPUT = '#register-password'
    PHONE_INPUT = '#register-phone'
    GET_STARTED_BUTTON = '#register-submit'
    REGISTER_PAGE_IDENTIFIER = '//h2[contains(text(), "Create Free Account")]'
    
    # Added missing validation locators
    SUCCESS_ELEMENT = '#success-toast' 
    TEMP_EMAIL_ERROR = '#error-toast'
    EMAIL_ERROR_MSG = '#email-validation-error'
    PASSWORD_ERROR_MSG = '//p[contains(text(), "Password does not meet validation requirements.")]'
    PHONE_ERROR_MSG = '//p[contains(text(), "Please enter a valid Phone number.")]'
    OTP_PAGE_IDENTIFIER = '//h2[contains(text(), "Verify Your OTP")]'
    OTP_INPUTS = "#otp-field-{index}"
    VERIFY_OTP_BUTTON = "#otp-submit"
    DASHBOARD_ELEMENT = '//h2[contains(text(), "Workspace")]'
    LOGIN_PAGE_IDENTIFIER = '//h2[contains(text(), "Login")]'

    def open_login_page(self):
        self.open(f"{Config.BASE_URL}/auth/login")

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
        self.page.locator(self.PHONE_INPUT).evaluate(
        "(element, value) => { element.removeAttribute('readonly'); element.value = value; element.dispatchEvent(new Event('input', { bubbles: true })); }",
        phone_number)

    def click_get_started(self):
        self.click(self.GET_STARTED_BUTTON)

    def signup(self, full_name: str, email: str, password: str, phone_number: str):
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_phone_number(phone_number)
        self.click_get_started()

    # Added methods requested by the Workflow
    def is_get_started_disabled(self):
        return self.page.locator(self.GET_STARTED_BUTTON).is_disabled()

    def is_get_started_enabled(self):
        return self.page.locator(self.GET_STARTED_BUTTON).is_enabled()

    def is_otp_page_visible(self):
        return self.is_visible(self.OTP_PAGE_IDENTIFIER,timeout=5000)

    def is_email_error_visible(self):
        return self.is_visible(self.EMAIL_ERROR_MSG)

    def is_password_error_visible(self):
        return self.is_visible(self.PASSWORD_ERROR_MSG ,timeout=5000)

    def is_phone_error_visible(self):
        return self.is_visible(self.PHONE_ERROR_MSG)

    def is_temp_email_error_visible(self):
        return self.is_visible(self.TEMP_EMAIL_ERROR, timeout=5000)

    def signup_successful(self):
        return self.is_otp_page_visible() or self.is_visible(self.SUCCESS_ELEMENT, timeout=5000)

    def temp_email_error_visible(self):
        return self.is_temp_email_error_visible()
    
    def enter_otp(self, otp: str):
        if len(otp) != 6:
            raise ValueError("OTP must be exactly 6 digits.")

        for index, digit in enumerate(otp, start=1):
            self.fill(self.OTP_INPUTS.format(index=index), digit)

    def click_verify_otp(self):
        self.click(self.VERIFY_OTP_BUTTON)
    
    def is_login_page_visible(self):
        return self.is_visible(self.LOGIN_PAGE_IDENTIFIER, timeout=10000)
    

    
