from playwright.sync_api import Page, expect, Locator
import time

class BasePage:
    """The parent class contains all common actions and is inherited by every Page Object."""
    def __init__(self, page: Page):
        self.page = page

    def _open_page(self, url: str):
        """Navigate to the specified URL."""
        print(f"[BasePage] Navigate to {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _wait_for_element(self, locator: str, timeout = 5000):
        """Auto wait for element"""
        return self.page.wait_for_selector(locator, timeout=timeout, state="visible")
    
    def _get_locator(self, locator: str) -> Locator:
        """Get the locator of the element."""
        return self.page.locator(locator)

    def _click(self, locator: str):
        """Execute the click action with proper error handling."""
        try:
            print(f"[Click] {locator}")
            self.page.locator(locator).click()
        except TimeoutError:
            print(f"[Error] Cannot click on {locator}")
            raise

    def _fill(self, locator: str, value: str):
        """Fill data into the input field."""
        print(f"Fill value {value} vào {locator}")
        self.page.locator(locator).fill(value)

    def _verify_text(self, locator: str, text: str):
        """Verify that the expected text is displayed on the interface."""
        expect(self.page.locator(locator)).to_contain_text(text)

    def _verify_placeholder(self, locator: str, text: str):
        expect(self.page.locator(locator)).to_have_attribute("placeholder", text)

    def _select_menu(self, text: str):
        """Select option on the menu."""
        locator = "//li//a//span[normalize-space()={text}]"
        self._click(locator)    
        
    def _take_screenshot(self, filename: str):
        """Capture and save a screenshot, typically used for pass/fail results."""
        path_file = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path_file)
        print(f"[SCREENSHOT] Lưu tại: {path_file}")    

    def _verify_locator_visible(self, locator: str):
        """Verify locator is existing on the form."""
        expect(self.page.locator(locator)).to_be_visible()
        print(f"[ASSERT]{locator} hiển thị thành công!")

    def _get_text(self, locator: str) -> str:
        return  self.page.locator(locator).inner_text()
    
    def _verify_url_contains(self, text: str):
        expect(self.page).to_have_url(text)



    