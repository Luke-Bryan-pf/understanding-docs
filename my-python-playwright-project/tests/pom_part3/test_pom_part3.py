# ✅ POM Framework - Part 3 | Creating HomePage and Locators

from pages.base_page import BasePage

class HomePage(BasePage):
    def click_get_started(self):
        self.page.click("text=Get Started")