from playwright.sync_api import expect
from playwright.sync_api import Playwright
from core.base_page import BasePage
import os

class Settings(BasePage):

    URL = "https://book.anhtester.com/user-management/setting-account"
    LIGHT_THEME = "//button[normalize-space()='Light']"
    DARK_THEME = "//button[normalize-space()='Dark']"
    SYSTEM_THEME = "//button[normalize-space()='System']"
    LIGHT_COLOR = "//div[@class='MuiBox-root css-505b0i']"
    DARK_COLOR = "//div[@class='MuiBox-root css-vpf2zm']"
    SYSTEM_COLOR = "//div[@class='MuiBox-root css-ck1li1']"
    SAVE_BTN = "//button[normalize-space()='Save']"
    RESET_BTN = "//button[normalize-space()='Reset']"
    PROFILE_ICON = "//img[@class='MuiAvatar-img css-45do71']"

    def __init__(self, page):
        super().__init__(page)

    def open_page_settings(self):
        self._open_page(self.URL, wait_until="domcontentloaded") 

    def verify_url(self):
        expect(self.page).to_have_url(self.URL)    

    def choose_light_color(self):
        self._click(self.LIGHT_COLOR)

    def choose_dark_color(self):
        self._click(self.DARK_COLOR)

    def choose_system_color(self):
        self._click(self.SYSTEM_COLOR)

    def select_btn_save(self):
        self._click(self.SAVE_BTN)
        self.page.wait_for_load_state("networkidle")

    def select_btn_reset(self):
        self._click(self.RESET_BTN)   

    def choose_change_theme(self, theme: str):
        if theme.lower() == "light":
           self._click(self.LIGHT_THEME)
        elif theme.lower() == "dark":
            self._click(self.DARK_THEME)
        elif theme.lower() == "system":
            self._click(self.SYSTEM_THEME)

    def assert_theme(self, theme):
        if theme == "system":
            expect(self.page.locator("html")).to_have_attribute("data-color-scheme", "light")
        else:    
            expect(self.page.locator("html")).to_have_attribute("data-color-scheme", theme)
