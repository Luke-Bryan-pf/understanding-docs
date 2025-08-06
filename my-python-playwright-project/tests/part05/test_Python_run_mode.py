#python

from playwright.sync_api import sync_playwright

def test_example_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()

if __name__ == "__main__":
    test_example_site()
