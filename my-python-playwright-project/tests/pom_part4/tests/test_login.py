# tests/test_login.py

from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.visit("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")