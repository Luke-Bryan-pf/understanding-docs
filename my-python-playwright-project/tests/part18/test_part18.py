# ✅ Nth Element Selector in Playwright

def test_nth_element(page):
    page.goto("https://demoqa.com/webtables")
    # Select the second row email field
    second_email = page.locator(".rt-tbody .rt-tr-group").nth(1).locator(".rt-td").nth(3)
    assert second_email.is_visible()
