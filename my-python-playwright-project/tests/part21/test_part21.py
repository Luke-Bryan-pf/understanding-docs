# ✅ Handle React Application Selectors in Playwright Python

def test_react_selector(page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.fill("#firstName", "John")
    page.fill("#lastName", "Doe")
    assert page.locator("#firstName").input_value() == "John"
