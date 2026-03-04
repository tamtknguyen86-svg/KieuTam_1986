from playwright.sync_api import Page, expect
from core.base_page import BasePage

class HomePage(BasePage):

    URL = "https://book.anhtester.com"
    # LOGO = "img[alt='ANHTESTER']"
    DASHBOARD_MENNU = "//span[normalize-space()='Dashboard']"
    USER_MENU = "//span[normalize-space()='User']"
    BOOK_MENU = "//span[normalize-space()='Book']"
    PROMOTION_MENU = "//span[normalize-space()='Promotion']"
    FILE_MENU = "//span[normalize-space()='File']"
    DATABASE_MENU = "//span[normalize-space()='Database']"
    BANNER_TEXT = "text=RESTful API"
    PROFILE_ICON = "//div[2]/div[2]/button"
    PROFILE_ON_PROFILE_ICON = "//li[normalize-space()='Profile']"
    SETTINGS_ON_PROFILE_ICON = "//li[normalize-space()='Settings']"
    

    def __init__(self, page):
        super().__init__(page)

    def verify_home_page(self):
        # """Verify LOGO visible"""
        # self._verify_locator_visible(self.LOGO)
        """Verify Dashboard menu visible"""
        self._verify_locator_visible(self.DASHBOARD_MENNU)
        # """Verify TITLE on Dashboard visible"""
        # self._verify_locator_visible(self.BANNER_TEXT)
        """Verify icon User Profile"""
        self._verify_locator_visible(self.PROFILE_ICON)

    def click_profile_icon_and_goto_profile(self):
        self._click(self.PROFILE_ICON)
        self._click(self.PROFILE_ON_PROFILE_ICON)

    def click_profile_icon_and_goto_settings(self):
        self._click(self.PROFILE_ICON)
        self._click(self.SETTINGS_ON_PROFILE_ICON)





        

