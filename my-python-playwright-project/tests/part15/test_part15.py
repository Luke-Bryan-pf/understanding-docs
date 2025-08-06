# ✅ Inspect Playwright Selectors in Chrome Dev Tools

def test_inspect_selectors(page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Test User")
    assert page.locator("#userName").input_value() == "Test User"
