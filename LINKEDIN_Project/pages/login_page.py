from core.base_page import BasePage, expect
import time, json

class LoginPage(BasePage):
    #Save locator & action of Login page

    URL = "https://www.linkedin.com/login"
    # PROFILE_ICON = ".MuiBox-root css-swawqt"
    # TITLE_LOCATOR = "//h3[normalize-space()='Sign in']"
    EMAIL_LOCATOR = "//input[@id='username']"
    # EMAIL_PLACEHOLDER = "Email address *"
    PASSWORD_LOCATOR = "//input[@id='password']"
    # PASSWORD_PLACEHOLDER = "Password *"
    LOGIN_BTN = "//button[@type='submit']"
    
    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self._open_page(self.URL)

    def check_form_login(self):
        self.goto()
        #CHECK 
        self._verify_locator_visible(self.TITLE_LOCATOR)
        self._verify_locator_visible(self.EMAIL_LOCATOR)
        self._verify_locator_visible(self.PASSWORD_LOCATOR)
        self._verify_locator_visible(self.LOGIN_BTN)

        # self._verify_text(self.TITLE_LOCATOR, self.TITLE_MESSAGE)
        # self._verify_placeholder(self.EMAIL_LOCATOR, self.EMAIL_PLACEHOLDER)
        # self._verify_placeholder(self.PASSWORD_LOCATOR, self.PASSWORD_PLACEHOLDER)
        self._verify_text(self.LOGIN_BTN,"Login account")

    def login_valid_user(self, email: str, password: str):
        self.goto()
        self._fill(self.EMAIL_LOCATOR, email)
        self._fill(self.PASSWORD_LOCATOR, password)
        self._click(self.LOGIN_BTN)

  