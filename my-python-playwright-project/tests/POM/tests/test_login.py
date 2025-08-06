# tests/POM/tests/test_login.py

from pages.login_page import LoginPage

def test_valid_login(page):
    page.set_viewport_size({"width": 1280, "height": 1024})
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    login = LoginPage(page)
    login.login("student", "Password123")

    assert page.locator("h1").text_content() == "Logged In Successfully"
