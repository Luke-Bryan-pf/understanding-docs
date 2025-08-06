# Test file for part03
# tests/part03/test_setup_check.py
from playwright.sync_api import sync_playwright

def test_setup_and_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # ✅ Use a specific browser
        page = browser.new_page()
        page.goto("https://example.com")
        print("Page title:", page.title())
        browser.close()
