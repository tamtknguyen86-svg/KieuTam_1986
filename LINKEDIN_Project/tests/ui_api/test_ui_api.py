from pages.login_page import LoginPage
import pytest, time
from playwright.sync_api import expect

def test_register_api_then_login_on_ui(page, registered_user):
    #Login by register account has just created by API
    login = LoginPage(page)
    login.goto()
    login.login_valid_user(registered_user["email"], registered_user["password"])
    print("Login succesfully!")
    time.sleep(4)

def test_verify_user_by_api(api_context, registered_user, auth_token, page):
    respond_user_login = api_context.post("/api/login",data={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })   
    assert respond_user_login.status == 200
    body = respond_user_login.json()
    assert "accessToken" in body
    assert body["accessToken"] is not None

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


