# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page  # Ensure page is accessible
        self.username_input = self.page.locator("#username")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("button[type='submit']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

