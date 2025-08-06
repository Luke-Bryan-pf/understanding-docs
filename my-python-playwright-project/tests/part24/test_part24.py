# ✅ Handle Web Table | HTML Table in Playwright Python

def test_web_table_read(page):
    page.goto("https://letcode.in/table")
    second_row_third_col = page.locator("//table//tbody/tr[2]/td[3]").nth(0)
    assert second_row_third_col.inner_text() != ""
