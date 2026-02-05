from playwright.sync_api import Browser

def load_session(browser: Browser, storage):
    return browser.new_context(storage_state=storage)

def save_session(context, path):
    context.storage_state(path=path)