# ✅ Selecting Visible Elements in Playwright Python

def test_visible_elements(page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#firstName:visible").fill("John")
    assert page.locator("#firstName").input_value() == "John"
