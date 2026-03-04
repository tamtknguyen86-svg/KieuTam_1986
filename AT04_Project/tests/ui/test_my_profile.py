from pages.login_page import LoginPage
from pages.home import HomePage
from pages.user_page import UserProfile
from playwright.sync_api import expect, Page
import random, os
import allure

@allure.description("Verify user can login and see dashboard.")
def test_verify_user_profile(logged_in_daskboard):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
        home.verify_home_page()
    with allure.step("Click icon profile and go to User Profile"):
        home.click_profile_icon_and_goto_profile()
        user_profile = UserProfile(logged_in_daskboard)
    with allure.step("Verify User Profle page"):     
        user_profile.verify_profile_loaded()

@allure.description("Verify update user info successfully.")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_user_info(logged_in_daskboard, page: Page):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
        home.verify_home_page()
        
    with allure.step("Click Icon Profile and go to Profile page"):   
        home.click_profile_icon_and_goto_profile() 
    with allure.step("Verify info profile page loading..."):       
        user_profile = UserProfile(page)
        user_profile.verify_profile_loaded()

    with allure.step("Random data user before updating"):
        new_name = "Tam QA"
        new_phone = f"09{random.randint(10000000, 99999999)}"
        new_address = "Tan Phu - HCM"

        user_profile.update_profile_info(
            name=new_name,
            phone=new_phone,
         address=new_address
        )
    with allure.step("Click button Save"):
        user_profile.click_save_button()
    with allure.step("Verify message toast after inputting user's info updated"):    
        user_profile.verify_toast_message_display()
    with allure.step("Verify info user after updating"):
        user_profile.verify_user_info(
            name=new_name,
            phone=new_phone,
            address=new_address    
        )

@allure.description("Verify user change avatar with .png")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_avatar_png(logged_in_daskboard):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
    # home.verify_home_page()
    with allure.step("Click Icon Profile and go to Profile page"):
        home.click_profile_icon_and_goto_profile()
        user_profile = UserProfile(logged_in_daskboard)
    with allure.step("Verify link profile's url"):    
        user_profile.verify_url()
    with allure.step("Upload file avatar"):
        avatar_path = os.path.abspath("data/avatar.png")
        user_profile.upload_file_avatar(avatar_path)
    with allure.step("Click button SAVE"):    
        user_profile.click_save_button()
    with allure.step("Verify toast message after upload avatar succesfully"): 
        user_profile.verify_toast_message_display()

@allure.description("Verify user change avatar with .jpg")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_avatar_jpg(logged_in_daskboard):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
    # home.verify_home_page()
    with allure.step("Click Icon Profile and go to Profile page"):
        home.click_profile_icon_and_goto_profile()
        user_profile = UserProfile(logged_in_daskboard)
    with allure.step("Verify link profile's url"):   
        user_profile.verify_url()
    with allure.step("Upload file avatar"):
        avatar_path = os.path.abspath("data/Baby.jpg")
        user_profile.upload_file_avatar(avatar_path)
    with allure.step("Click button SAVE"):   
        user_profile.click_save_button()
    with allure.step("Verify toast message after upload avatar succesfully"):    
        user_profile.verify_toast_message_display()    

@allure.description("Verify user change avatar with file > 3 Mb")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_avatar_larger_3M(logged_in_daskboard):
    with allure.step("Login successfully and go to Daskboard"):
        home = HomePage(logged_in_daskboard)
    # home.verify_home_page()
    with allure.step("Click Icon Profile and go to Profile page"):
        home.click_profile_icon_and_goto_profile()
    with allure.step("Verify link profile's url"):       
        user_profile = UserProfile(logged_in_daskboard)
        user_profile.verify_url()
    with allure.step("Upload file avatar"):
        avatar_path = os.path.abspath("data/File_5M6.png")
        user_profile.upload_file_avatar(avatar_path)
    with allure.step("Click button SAVE"): 
        user_profile.click_save_button()
    with allure.step("Verify toast message after upload avatar succesfully"):    
        user_profile.verify_toast_message_display()
