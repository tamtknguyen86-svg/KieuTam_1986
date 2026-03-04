from pages.login_page import LoginPage
import pytest, time
from playwright.sync_api import expect
import allure

@allure.description("Verify login successfully with valid account")
def test_register_api_then_login_on_ui(page, registered_user):
    #Login by register account has just created by API
    with allure.step("Open page Login"):
        login = LoginPage(page)
        login.open_page()
    with allure.step("Login successfully with valid account"):    
        login.login_valid_user(registered_user["email"], registered_user["password"])
        print("Login succesfully!")

@allure.description("Verify login with acc register by API")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_user_by_api(api_context, registered_user, auth_token, page):
    with allure.step("Get API acc register"):
        respond_user_login = api_context.post("/api/login",data={
            "email": registered_user["email"],
            "password": registered_user["password"]
        })   
    with allure.step("Verify respond's status"):    
        assert respond_user_login.status == 200
    with allure.step("Verify body's info "):      
        body = respond_user_login.json()
        assert "accessToken" in body
        assert body["accessToken"] is not None
    with allure.step("Get respond's API "):
        resp = api_context.get("/api/me",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        
    assert resp.status == 200
    body = resp.json()
    assert body["email"] == registered_user["email"]

    page.add_init_script(
        f"""
        localStorage.setItem("accessToken", "{auth_token}");
        """
    )   
    page.goto("https://book.anhtester.com/user-management/my-profile", wait_until="domcontentloaded")

    email_value = page.locator("//input[@name='email']")
    email_value.wait_for(state="visible")

    expect(email_value).not_to_have_value("", timeout=10000)

    email = email_value.input_value()

    assert body["email"] == email


