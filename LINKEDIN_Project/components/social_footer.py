from core.base_page import BasePage, expect
from playwright.sync_api import Playwright
import time


class Social_Footer(BasePage):

    # ICONS = {
    #     "linkedin": "//a[@target='_blank'][1]",
    #     "facebook": "//a[@target='_blank'][2]",
    #     "twister": "//a[@target='_blank'][3]",
    #     "youtube": "//a[@target='_blank'][4]"
    # }
    BTN_CLOSE_POPUP_FACEBOOK = "div[aria-label='Close'], div[aria-label='Đóng']"
    URL_TWISTER = "https://x.com/orangehrm?lang=en"
    URL_FACEBOOK = "https://www.facebook.com/OrangeHRM/"
    URL_YOUTUBE = "https://www.youtube.com/c/OrangeHRMInc"


    def __init__(self, page):
        super().__init__(page)

    def open_icon_new_tab(self, icon_name):
        with self.page.context.expect_page() as new_windown_page:
            self.page.click(self.ICONS[icon_name])
        new_tab = new_windown_page.value
        new_tab.wait_for_load_state()
        return new_tab        

    def verify_twister_page(self, twister_page):
        expect(twister_page.locator("a[aria-label='X']")).to_be_visible()
        expect(twister_page.get_by_role("heading",name="OrangeHRM")).to_be_visible()
            
    def verify_facebook_page(self, facebook_page):
        # Close popup facebook if it shows
        self._take_screenshot("Facebook_1")
        if self.page.locator(self.BTN_CLOSE_POPUP_FACEBOOK).is_visible(timeout=2000):
            self.page.locator(self.BTN_CLOSE_POPUP_FACEBOOK).click()
            print("Close popup facebook is successfully!")
        expect(facebook_page.locator("//div[@aria-label='Facebook']")).to_be_visible()
        expect(facebook_page.locator("h1",has_text="OrangeHRM - World's Most Popular Opensource HRIS")).to_be_visible()
        self._take_screenshot("Facebook_2")

    def verify_lindln_page(self, lindln_page):
        expect(lindln_page.locator("li-icon[aria-label='LinkedIn']")).to_be_visible()
        expect(lindln_page.get_by_role("h1",has_text="OrangeHRM")).to_be_visible()

    def verify_youtube_page(self, youtube_page):
        expect(youtube_page.locator("//span[normalize-space()='OrangeHRM Inc']")).to_be_visible()
        print("Youtube's title is OrangeHRM Inc")