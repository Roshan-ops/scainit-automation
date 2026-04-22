from pages.base_page import BasePage
from utils.config import Config

class LoginPage(BasePage):
    EMAIL_INPUT = '#login-email'
    PASSWORD_INPUT = '#login-password'
    LOGIN_BUTTON = '#login-submit'
    DASHBOARD_ELEMENT = '//h1[contains(text(), "Your AI Workspace")]'
    ERROR_MESSAGE = '//p[contains(text(), "Invalid Credentials")]'

    def navigate(self):
        self.open(f"{Config.BASE_URL}/login")

    def login(self, email: str, password: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def dashboard_visible(self):
        return self.is_visible(self.DASHBOARD_ELEMENT, timeout=10000)

    def error_visible(self):
        return self.is_visible(self.ERROR_MESSAGE, timeout=10000)