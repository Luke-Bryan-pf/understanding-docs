# ✅ Handle ShadowDom Elements in Playwright Python
def test_shadow_dom(page):
    page.goto("https://books-pwakit.appspot.com/")

    # Wait for the shadow root to be ready
    search_box = page.locator("book-app").locator("book-input-decorator >>> input#input")

    search_box.fill("Playwright")
    assert search_box.input_value() == "Playwright"
