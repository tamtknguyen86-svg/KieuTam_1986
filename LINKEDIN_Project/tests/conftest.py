import pytest, json, random, string, time
from playwright.sync_api import Playwright
from playwright.sync_api import Browser
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p
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

# -------------------------
# Login Page
# -------------------------
@pytest.fixture
def login_page(page):
    return LoginPage(page)

#2. Fixture logged (optional)
@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.login_valid_user()
    return page
# -------------------------
# Fixture for iphone 13
# -------------------------

@pytest.fixture(scope="function")
def brownser_for_iphone13(playwright_instance):
    p = playwright_instance

    browser = p.webkit.launch(headless=False)
    device = p.devices["iPhone 13"]

    context = browser.new_context(
        **device,
        locale="en-US",
        storage_state="auth_mobile.json"  # reuse login
    )

    page = context.new_page()

    yield page

    context.close()
    browser.close()

@pytest.fixture(params=["iPhone 13", "Galaxy S9"])
def mobile_page(playwright_instance, request):
    p = playwright_instance
    browser = p.chromium.launch(headless=False)
    device = p.devices[request.param]

    context = browser.new_context(**device)
    page = context.new_page()

    yield page

    context.close()
    browser.close()    
