
# Part 17: Matching Conditions Using XPath Union

## Definition
XPath allows using the **`|` (union operator)** to match **one of multiple conditions**.

## Example:
```xpath
//div[@id='login'] | //div[@id='signup']
```
Matches either the login OR signup div.

In this test, we match both "Text Box" and "Check Box" links using XPath union.
