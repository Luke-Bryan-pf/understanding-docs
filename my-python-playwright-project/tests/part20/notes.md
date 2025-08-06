
# Part 20: Dynamic Dropdown Selection

## Definition
Dynamic dropdowns (like React/Angular components) require typing text and pressing Enter — they don't use `<select>` tags.

## Steps:
1. Click into the input
2. Type desired value
3. Press Enter

This test selects a value from a React-based dropdown.
--- 
Topic Summary:
This part teaches how to work with dynamic dropdowns, where the dropdown values are loaded via JavaScript or APIs after user input (e.g., typing into a search box).

Common steps:

Type input into the dropdown field.
Wait for dropdown options to load.
Select the desired option based on visible text.

Example:
page.locator("#autoCompleteMultipleInput").fill("Red")
page.locator("div.auto-complete__option >> text=Red").click()

Why it's useful:
Real-world apps often use autocomplete 
Knowing how to interact with these helps automate more complex UIs.
