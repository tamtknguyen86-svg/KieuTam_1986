from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.job_page import JobsPage
from pages.easy_apply import EasyApply
import logging


def test_easy_apply_on_browser(login_page, page):
    login_page.login_valid_user("tamtknguyen86@gmail.com","Aloha@1000")

    try:
        jobs = JobsPage(page)
        jobs._open_page("https://www.linkedin.com/jobs")
        jobs.search_job("QA Engineer")
        jobs.filter_easy_apply()
        jobs.open_first_job()

        page.click("//button[@id='jobs-apply-button-id']")

        easy_apply =  EasyApply(page)
        # missing = easy_apply.verify_required_fields()
        # if missing:
        #     logging.error(f"Missing fields: {missing}")

        # assert easy_apply.is_submit_disabled() is True
        easy_apply.verify_form_apply_and_close_form()

    except Exception as e:
        logging.error(str(e))
        raise
    
# def test_easy_apply_mobile_iphone13(brownser_for_iphone13):
#     page = brownser_for_iphone13

#     jobs = JobsPage(page)
#     jobs._open_page("https://www.linkedin.com/jobs")
#     jobs.search_job("QA Engineer")
#     jobs.filter_easy_apply()
#     jobs.open_first_job()

#     page.tap("//button[@id='jobs-apply-button-id']")

#     easy_apply = EasyApply(page)

#     easy_apply.verify_form_apply_and_close_form()

