from core.base_page import BasePage

class JobsPage(BasePage):
    SEARCH_BOX = "//input[@componentkey='jobSearchBox']"
    EASY_APPLY_FILTER = "//span[text()='Easy Apply']"
    FIRST_JOB = "(//div[contains(@class,'job-card-container')])[1]"

    def search_job(self, keyword):
        self.page.fill(self.SEARCH_BOX, keyword)
        self.page.keyboard.press("Enter")

    def filter_easy_apply(self):
        self.page.click(self.EASY_APPLY_FILTER)

    def open_first_job(self):
        self.page.click(self.FIRST_JOB)
