
# Part 09: Locators in Playwright

Locators are more reliable than CSS/XPath because they wait and retry automatically.

```python
page.locator("text=Submit")
page.locator("css=button.submit")
```

Use `get_by_*` methods for semantic targeting.
