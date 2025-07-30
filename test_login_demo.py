from playwright.sync_api import sync_playwright

def test_login_to_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to login page
        page.goto("https://www.saucedemo.com")

        # Fill in the username and password fields
        page.fill("input#user-name", "standard_user")
        page.fill("input#password", "secret_sauce")

        # Click the login button
        page.click("input#login-button")

        # Wait for the products page to load
        page.wait_for_selector(".inventory_list")

        # Assert that login was successful by checking for a product
        assert page.locator(".inventory_item").count() > 0

        browser.close()

def test_login_failure_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        page.fill("input#user-name", "invalid_user")
        page.fill("input#password", "wrong_password")
        page.click("input#login-button")

        # Intentionally failing assertion
        assert "Login successful" in page.content()

        browser.close()
