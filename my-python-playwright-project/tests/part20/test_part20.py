# ✅ Dynamic Dropdown Values Select in Playwright Python

def test_dynamic_dropdown(page):
    page.goto("https://demoqa.com/select-menu", timeout=60000, wait_until="domcontentloaded")
    page.locator("div#withOptGroup").click()
    page.get_by_text("Group 2, option 1").click()

    selected = page.locator("div.css-1uccc91-singleValue")
    assert selected.inner_text() == "Group 2, option 1"

