# ✅ Xpath Locators in Playwright Python

def test_xpath_locator(page):
    page.goto("https://demoqa.com/elements")
    locator = page.locator("xpath=//span[text()='Text Box']")
    locator.click()
    assert page.url.endswith("text-box")
