from playwright.sync_api import Playwright
from core.base_page import BasePage
import re, time

class DashBoard(BasePage):


    def __init__(self, page):
        super().__init__(page)