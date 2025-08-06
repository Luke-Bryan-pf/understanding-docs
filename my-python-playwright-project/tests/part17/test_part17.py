# ✅ Matching one of the condition using CSS | XPath Union

def test_xpath_union(page):
    page.goto("https://demoqa.com/elements")
    # XPath Union: Match either 'Text Box' or 'Check Box'
    locator = page.locator("xpath=//span[text()='Text Box'] | //span[text()='Check Box']")
    assert locator.count() >= 1
