from core.base_page import BasePage, expect
import time, json

class LoginPage(BasePage):
    #Save locator & action of Login page

    URL = "https://book.anhtester.com/sign-in"
    PROFILE_ICON = ".MuiBox-root css-swawqt"
    TITLE_LOCATOR = "//h3[normalize-space()='Sign in']"
    EMAIL_LOCATOR = "//input[@name='email']"
    EMAIL_PLACEHOLDER = "Email address *"
    PASSWORD_LOCATOR = "//input[@name='password']"
    PASSWORD_PLACEHOLDER = "Password *"
    LOGIN_BTN = "//button[@type='submit']"

    TITLE_TEXT = "Sign in"
    TEXT_NOT_ACCOUNT_LOCATOR = "//a[@href='/sign-up']"
    CONTENT_NOT_ACCOUNT = "Don't have an account?"
    TEXT_SIGN_UP_LOCATOR = "//a[@href='/sign-up']"
    CONTENT_SIGN_UP = "Get started"
    HELP_LOCATOR = "//div[@class='MuiContainer-root css-1lquw9y']//font[@dir='auto']/font"

    
    def __init__(self, page):
        super().__init__(page)

    def open_page(self):
        self._open_page(self.URL)
        self._take_screenshot("Open_login_page")

    def load_credentials(self):
        with open("data/credentials.json","r") as f:
            return json.load(f)    

    def check_form_login(self):
        self.open_page()
        #CHECK 
        self._verify_locator_visible(self.TITLE_LOCATOR)
        self._verify_locator_visible(self.EMAIL_LOCATOR)
        self._verify_locator_visible(self.PASSWORD_LOCATOR)
        self._verify_locator_visible(self.LOGIN_BTN)

        self._verify_text(self.TITLE_LOCATOR, self.TITLE_TEXT)
        self._verify_placeholder(self.EMAIL_LOCATOR, self.EMAIL_PLACEHOLDER)
        self._verify_placeholder(self.PASSWORD_LOCATOR, self.PASSWORD_PLACEHOLDER)
        self._verify_text(self.LOGIN_BTN,"Login account")

    def login_valid_user(self):
        self.open_page()
        creds = self.load_credentials()
        self._fill(self.EMAIL_LOCATOR, creds["valid_user"]["email"])
        self._fill(self.PASSWORD_LOCATOR, creds["valid_user"]["password"])
        self._click(self.LOGIN_BTN)
        self._take_screenshot("Dashboard")

    