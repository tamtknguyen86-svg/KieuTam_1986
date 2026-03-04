from pages.login_page import LoginPage
from pages.home import HomePage
from pages.settings_page import Settings
from playwright.sync_api import expect, Page
import random, os
import allure


@allure.description("Verify update user info successfully.")
@allure.severity(allure.severity_level.CRITICAL)
def test_choose_dark_theme(logged_in_daskboard, page: Page):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
        home.verify_home_page()
    with allure.step("Click icon profile and go to Settings page"):    
        home.click_profile_icon_and_goto_settings()
    with allure.step("Verify link Setting's url"):    
        settings = Settings(logged_in_daskboard)
        settings.verify_url()
    with allure.step("Choose change theme: Dark"):
        settings.choose_change_theme("dark")
    with allure.step("Choose color"):    
        settings.choose_dark_color()
    with allure.step("Click button SAVE"):
        settings.select_btn_save()
    with allure.step("Verify theme change to Dark theme successfully!"):
        settings.assert_theme("dark")

def test_choose_light_theme(logged_in_daskboard, page: Page):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
    with allure.step("Verify Home page"):    
        home.verify_home_page()
    with allure.step("Click icon profile and go to Settings page"):      
        home.click_profile_icon_and_goto_settings()
    with allure.step("Verify link Setting's url"):     
        settings = Settings(logged_in_daskboard)
        settings.verify_url()
    with allure.step("Choose change theme: Light"):
        settings.choose_change_theme("light")
    with allure.step("Choose color"):    
        settings.choose_light_color()
    with allure.step("Click button SAVE"):
        settings.select_btn_save()
    with allure.step("Verify theme change to Light theme successfully!"):
        settings.assert_theme("light")

def test_choose_system_theme(logged_in_daskboard, page: Page):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
    with allure.step("Verify Home page"):       
        home.verify_home_page()
    with allure.step("Click icon profile and go to Settings page"):     
        home.click_profile_icon_and_goto_settings()
    with allure.step("Verify link Setting's url"):      
        settings = Settings(logged_in_daskboard)
        settings.verify_url()
    with allure.step("Choose change theme: System"):
        settings.choose_change_theme("system")
    with allure.step("Choose color"):
        settings.choose_system_color()
    with allure.step("Click button SAVE"):
        settings.select_btn_save()
    with allure.step("Verify theme change to System theme successfully!"):
        settings.assert_theme("system")





