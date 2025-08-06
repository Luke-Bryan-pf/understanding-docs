# ✅ Text Selector in Playwright | Finding Elements in Web Page

def test_text_selector(page):
    page.goto("https://example.com")
    page.click("text=More information")
    assert "iana.org" in page.url
