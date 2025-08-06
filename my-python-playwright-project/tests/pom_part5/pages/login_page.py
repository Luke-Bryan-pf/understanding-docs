# pages/login_page.py

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.success_message = page.locator("text=Logged In Successfully")
        self.error_message = page.locator("#error")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_successful(self):
        assert self.success_message.is_visible()

    def assert_login_failed(self):
        assert self.error_message.is_visible()