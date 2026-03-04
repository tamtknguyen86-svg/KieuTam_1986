from playwright.sync_api import expect
from playwright.sync_api import Playwright
from core.base_page import BasePage
import os

class UserProfile(BasePage):

    URL = "https://book.anhtester.com/user-management/my-profile"
    # Information section
    # AVATAR_UPLOAD = "//div[@class='MuiStack-root css-o7ghod']"
    AVATAR_UPLOAD = "//input[@name='avatar' and @type='file']"
    # AVATAR_IMAGE = "//img[contains(@src,'data:image') or contains(@src,'avatar')]"
    NAME_INPUT = "//input[@name='name']"
    PHONE_INPUT = "//input[@name='phone']"
    DIVISION_DROPDOWN = "//div//input[@id='address-division']"
    WARD_DROPDOWN = "//div//input[@id='address-ward']"
    ADDRESS_TEXTAREA = "//textarea[@id='address']"
    # Account section
    EMAIL_INPUT = "//div//input[@name='email']"
    OLD_PASSWORD_INPUT = "//div//input[@name='oldPassword']"
    PASSWORD_INPUT = "//div//input[@name='password']"
    PASSWORD_CONFIRM_INPUT = "//div//input[@name='password_confirmation']"
    # button
    RESET_BTN = "//button[normalize-space()='Reset']"
    SAVE_PROFILE_BTN = "//button[normalize-space()='Save Profile']"
    TOAST_UPDATE_SUCCESSFULLY = "//div//p[normalize-space()='Updated profile successfully.']"
    TOAST_BUTTON_CLOSE = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-a16rv9']"
    

    def __init__(self, page):
        super().__init__(page)

    def open_page_profile(self):
        self._open_page(self.URL, wait_until="domcontentloaded")    

    def verify_profile_loaded(self):
        # self._verify_url_contains(self.URL)
        """Verify Information section"""
        self._verify_locator_visible(self.NAME_INPUT)
        self._verify_locator_visible(self.PHONE_INPUT)
        self._verify_locator_visible(self.DIVISION_DROPDOWN)
        self._verify_locator_visible(self.WARD_DROPDOWN)
        self._verify_locator_visible(self.ADDRESS_TEXTAREA)
        """Verify Account section"""
        self._verify_locator_visible(self.EMAIL_INPUT)
        self._verify_locator_visible(self.OLD_PASSWORD_INPUT)
        self._verify_locator_visible(self.PASSWORD_INPUT)
        self._verify_locator_visible(self.PASSWORD_CONFIRM_INPUT)

    def click_save_button(self):
        self._scroll_to_view(self.SAVE_PROFILE_BTN)
        self._click(self.SAVE_PROFILE_BTN)

    def verify_toast_message_display(self):
        self._verify_locator_visible(self.TOAST_UPDATE_SUCCESSFULLY)
        self._take_screenshot("Update_Name_successfully")
        self._click(self.TOAST_BUTTON_CLOSE)

    def verify_user_info(self, name:str, phone:str, address:str):
        self._verify_value_on_text(self.NAME_INPUT, name)
        self._verify_value_on_text(self.PHONE_INPUT, phone)
        # self._verify_value_on_text(self.ADDRESS_TEXTAREA, address)

    def verify_update_name(self, expected_name: str):
        self._fill(self.NAME_INPUT, expected_name)
        self.click_save_button()
        self.toast_message_display()
        # Verify name after updating successfully
        self._verify_value_on_text(self.NAME_INPUT, expected_name)
        name_current = self._get_text(self.NAME_INPUT)
        print(f"Currently, Name is {name_current}")

    # ===== Update profile with 1 or 2 or 3 or all info =====
    def update_profile_info(self, name=None, phone=None, address=None):
        if name:
            self._fill(self.NAME_INPUT, name)

        if phone:
            self._scroll_to_view(self.PHONE_INPUT)
            self._fill(self.PHONE_INPUT, phone)

        # if address:
        #     self._scroll_to_view(self.ADDRESS_TEXTAREA)
        #     self._fill(self.ADDRESS_TEXTAREA, address)
    # ===== Verify updated values =====        
    def verify_update_values_on_profile(self, name=None, phone=None, address=None):
        if name:
            self._verify_value_on_text(self.NAME_INPUT, name)
        if phone:
            self._verify_value_on_text(self.PHONE_INPUT, phone)
        # if address:
        #     self._verify_value_on_text(self.ADDRESS_TEXTAREA, address)


    # ===== Upload avatar png =====
    def upload_file_avatar(self, avatar_path):
        # avatar_path = os.path.abspath("data/avatar.png")
        assert os.path.exists(avatar_path), "Avatar file not found"

        # self._click(self.AVATAR_UPLOAD)
        self.page.locator(self.AVATAR_UPLOAD).set_input_files(avatar_path)
        # self.page.wait_for_timeout(2000)

        print(f"Upload file avatar {avatar_path} successfully")

    # ===== Upload avatar jpg =====
    def upload_file_avatar_jpg(self):
        avatar_path = os.path.abspath("data/Baby.jpg")
        assert os.path.exists(avatar_path), "Avatar file not found"

        # self._click(self.AVATAR_UPLOAD)
        self.page.locator(self.AVATAR_UPLOAD).set_input_files(avatar_path)
        # self.page.wait_for_timeout(2000)

        print(f"Upload file avatar {avatar_path} successfully")    

        # ===== Upload avatar jpg =====
    def upload_file_avatar_larger3M(self):
        avatar_path = os.path.abspath("data/File_5M6.png")
        assert os.path.exists(avatar_path), "Avatar file not found"

        # self._click(self.AVATAR_UPLOAD)
        self.page.locator(self.AVATAR_UPLOAD).set_input_files(avatar_path)
        # self.page.wait_for_timeout(2000)

        print(f"Upload file avatar {avatar_path} successfully")        

    def verify_url(self):
        self._verify_url_contains(self.URL)    