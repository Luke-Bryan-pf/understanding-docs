# ✅ Create Element and Elements in Playwright | Locators

def test_locators(page):
    page.goto("https://example.com")
    locator = page.locator("h1")
    assert locator.inner_text() == "Example Domain"
