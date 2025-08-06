# pages/login_page.py

from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Submit")

    def login(self, username, password):
        self.username_input.wait_for(state="visible")
        self.username_input.fill(username)

        self.password_input.wait_for(state="visible")
        self.password_input.fill(password)

        self.login_button.wait_for(state="attached")  # Ensure it's in DOM
        self.login_button.scroll_into_view_if_needed(timeout=5000)  # Optional
        self.login_button.click(timeout=10000)  # Wait up to 10 seconds to click
