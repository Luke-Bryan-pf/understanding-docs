from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()

def test_bing_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.bing.com")
        assert "Bing" in page.title()
        browser.close()

def test_duckduckgo_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://duckduckgo.com")
        assert "DuckDuckGo" in page.title()
        browser.close()

def test_github_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://github.com")
        assert "GitHub" in page.title()
        browser.close()

#failure test to demonstrate error handling
def test_wrong_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Not Google" in page.title()  # Intentionally wrong
        browser.close()


