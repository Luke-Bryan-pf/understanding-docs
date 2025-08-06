# Test file for part02
from playwright.sync_api import sync_playwright

def test_supported_browsers():
    with sync_playwright() as p:
        print("✅ Browsers Available:")
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto("https://example.com")
            print(f"{browser_type.name}: {page.title()}")
            browser.close()

# pytest -s tests/part02/test_browser_support.py
