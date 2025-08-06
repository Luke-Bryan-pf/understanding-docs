# ✅ Mouse Actions | Mouse Hover | Double Click | Drag And Drop

def test_mouse_actions(page):
    page.goto("https://demoqa.com/buttons")
    page.dblclick("xpath=//button[text()='Double Click Me']")
    assert page.locator("#doubleClickMessage").is_visible()
