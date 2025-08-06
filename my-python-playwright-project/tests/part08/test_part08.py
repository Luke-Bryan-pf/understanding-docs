# ✅ Browser Context | Multiple Browser Context

def test_multiple_contexts(browser):
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://example.com")

    context2 = browser.new_context()
    page2 = context2.new_page()
    page2.goto("https://example.com")

    assert page1.url == page2.url
