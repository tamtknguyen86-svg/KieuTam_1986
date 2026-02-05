from core.base_page import BasePage

class EasyApply(BasePage):
    # FIRSTNAME = "//input[contains(@id,'firstName')]"
    EMAIL = "//input[@type='email']"
    # UPLOAD_CV = "//input[type='file']"
    SUBMIT_BTN = "//button[@aria-label='Continue to next step']"
    CLOSE_BTN = "(//*[name()='use'][@href='#close-medium'])[1]"

    def verify_required_fields(self):
        missing = []
        for field, name in [
            (self.FIRSTNAME, "First name*"),
            (self.EMAIL, "Email")
        ]:
            if not self.page.locator(field).is_visible():
                missing.append(name)
        return missing
    
    def upload_resume(self, file_path):
        self.page.set_input_files(self.UPLOAD_CV, file_path)

    def is_submit_disabled(self):
        return self.page.locator(self.SUBMIT_BTN).is_disabled() 

    def verify_form_apply_and_close_form(self):
        self._click(self.CLOSE_BTN)
        
