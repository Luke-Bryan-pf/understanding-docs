# Part 6 - Inspector | Record & play with debugging using codegen

## Goal:
- Demonstrate: Inspector | Record & play with debugging using codegen

How to run :
pytest tests/part06/test_codegen_example.py

##  Sample Test
```python
def test_example(page: Page) -> None:
    page.goto("https://example.com/")
    page.get_by_role("link", name="More information...").click()
    page.get_by_role("link", name="IANA-managed Reserved Domains").click()
    page.get_by_role("link", name="RFC 2606").click()
    page.get_by_role("link", name="RFC 1035").click()
