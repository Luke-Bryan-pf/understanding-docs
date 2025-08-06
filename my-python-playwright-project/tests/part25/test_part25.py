# Handle Complex Dynamic Web Table | HTML Table

def test_handle_dynamic_table(page):
    # Step 1: Navigate to the dynamic table page
    page.goto("https://letcode.in/table", timeout=60000, wait_until="domcontentloaded")

    # Step 2: Locate all rows in the first table
    rows = page.locator("table#simpletable tbody tr")

    # Step 3: Iterate and print each row's text content
    for i in range(rows.count()):
        row_text = rows.nth(i).inner_text()
        print(f"Row {i + 1}: {row_text}")

    # Step 4: Example: Tick the checkbox for "Raj"
    for i in range(rows.count()):
        row = rows.nth(i)
        if "Raj" in row.inner_text():
            row.locator("input[type='checkbox']").check()
            break

    # Step 5: Assert checkbox is checked for Raj
    raj_checkbox = page.locator("table#simpletable tbody tr").filter(has_text="Raj").locator("input[type='checkbox']")
    assert raj_checkbox.is_checked()
