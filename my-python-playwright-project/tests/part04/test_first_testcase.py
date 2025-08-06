# Test file for part04
# Python Playwright Beginner[2023] Part 4: Create First Test Case using Playwright Python
from playwright.sync_api import sync_playwright

def test_example_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Show browser
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()
