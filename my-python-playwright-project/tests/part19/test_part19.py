# ✅ How to Select Dropdown values in Playwright Python

def test_dropdown_select(page):
    page.goto("https://demoqa.com/select-menu")
    page.select_option("#oldSelectMenu", label="Purple")
    selected = page.locator("#oldSelectMenu").input_value()
    assert selected == "4"
