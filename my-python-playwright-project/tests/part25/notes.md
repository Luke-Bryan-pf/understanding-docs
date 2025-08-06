
# Part 25: Handling Complex Dynamic Tables

# Definition
Dynamic tables are updated using JavaScript and may require interacting with inputs inside table rows.
This test interacts with a dynamic form-like structure as a simple illustration of dynamic table-like behavior.

For example, you may need to find a value in one cell and perform an action in a related cell.

# Techniques:
Use XPath or chained locators to:
Find a row containing specific text
Click buttons or extract info from adjacent columns

Example:
# Find row where name is "Alden" and click delete in that row
row = page.locator("//div[@role='row']").filter(has_text="Alden")
row.locator("button[title='Delete']").click()

# Why it's useful:
Many dashboards and admin panels use data tables.
Automating table interactions is critical for real test coverage.