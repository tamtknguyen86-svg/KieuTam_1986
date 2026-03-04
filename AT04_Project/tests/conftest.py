import pytest, json, random, string, time
from playwright.sync_api import Playwright
from page_api.authentication_api import AuthAPI
from page_api.user_api import UserAPI
from pages.login_page import LoginPage
from pages.user_page import UserProfile
# -------------------------
# Random email & password
# -------------------------
def random_email():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # num = int(time.time())
    return f"kieutam_{suffix}@mailqa.com"

def random_password():
    return "abc@ABC123" #demo; 
# -------------------------
# API Context (Playwright request)
# -------------------------

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url ="https://book.anhtester.com",
        extra_http_headers={
            "Accept":"application/json",
            "Content-Type": "application/json",
        }    
    )
    yield request_context
    #Purpose : clear cache, memory after using
    request_context.dispose()

# -------------------------
# Test Data
# -------------------------
@pytest.fixture
def new_user_data():
    return {
        "email": random_email(),
        "name": "KieuTam",
        "password": random_password(),
        "phone": "0981110001",
        "address": "HCM",
        "avatarUrl": ""
    }

# -------------------------
# API Fixtures
# -------------------------
@pytest.fixture
def registered_user(api_context, new_user_data):
    resp = api_context.post("api/register",data=new_user_data)
    assert resp.status in [200, 201]
    return new_user_data

@pytest.fixture
def login_get_token(api_context, registered_user):
    resp = api_context.post("/api/login", data={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    assert resp.status == 200
    body = resp.json()
    assert "accessToken" in body
    return  body["accessToken"]

@pytest.fixture
def api_user(api_context):
    return UserAPI(api_context)

@pytest.fixture
def api_auth(api_context):
    return AuthAPI(api_context)

@pytest.fixture
def user_session(api_context, new_user_data):
    """
    1. Register
    2. Login -> token
    yield: user + token
    teardown: logout before clean
    """
    # Register
    register_resp = api_context.post("/api/register", data=new_user_data)
    assert register_resp.status in [200, 201], \
        f"Register failed: {register_resp.status} - {register_resp.text()}"

    # Login
    login_resp = api_context.post("/api/login", data={
        "email": new_user_data["email"],
        "password": new_user_data["password"]
    })
    assert login_resp.status == 200, f"Login failed: {login_resp.status} - {login_resp.text()}"
    token = login_resp.json().get("accessToken")
    assert token, "Token is empty"

    yield {
        "user": new_user_data,
        "token": token
    }
    # Teardown
    try:
        api_context.delete("/api/logout", headers={"Authorization": f"Bearer {token}"})
    except Exception as e:
        print(f"[Teardown] Logout failed but ignored: {e}")

# -------------------------
# Fixtures for web application fixture: brownser, context, new page
# -------------------------
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def login(page):
    return LoginPage(page)

@pytest.fixture
def logged_in_daskboard(page):
    log_in = LoginPage(page)
    log_in.login_valid_user()
    return page

@pytest.fixture(scope="function")
def logged_in_profile(page):
    login_page = LoginPage(page)
    login_page.login_valid_user()
    user_profile = UserProfile(page)
    user_profile.open_page_profile()

    yield user_profile

  




